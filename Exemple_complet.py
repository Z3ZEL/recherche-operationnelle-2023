#chemin relatif vers le fichier (l'utilisation .. permet de revenir au dossier parent)
datafileName = 'data_CWFL/cap41.txt'

#ouverture du fichier, le ferme automatiquement à la fin et gère les exceptions
with open(datafileName, "r") as file:
    # lecture de la 1ère ligne et séparation des éléments de la ligne
    # dans un tableau en utilisant l'espace comme séparateur
    line = file.readline()  
    lineTab = line.split()
    
    # la valeur de la 1ère case correspond au nombre d'entrepôts
    # (attention de penser à convertir la chaîne de caractère en un entier)
    nb_warehouses = int(lineTab[0])

    # la valeur de la 2ème case correspond au nombre de clients
    nb_customers = int(lineTab[1])

    # création d'un tableau qui stockera les capacités des entrepôts
    capacity = []
    # création d'un tableau qui stockera les coûts d'ouverture des entrepôts
    opening_cost = []
    
    # pour chaque ligne contenant les informations sur les entrepôts
    for i in range(nb_warehouses):
        # lecture de la ligne suivante et séparation des éléments de la ligne
        # dans un tableau en utilisant l'espace comme séparateur
        line = file.readline()
        lineTab = line.split()
        
        # ajout de l'élément de la 1ère case au tableau qui contient les capacités 
        capacity.append(int(lineTab[0])) 
        # ajout de l'élément de la 2ème case au tableau qui contient les coûts d'ouverture 
        opening_cost.append(float(lineTab[1]))
    
    # création d'un tableau qui stockera les demandes des clients
    demand = [] 
    # création d'un tableau qui stockera les tableaux de coûts d'affectation aux entrepôts de chaque client
    assignment_cost = []
    
    # pour chaque ligne contenant les informations sur les clients
    for j in range(nb_customers):
        # lecture de la ligne suivante
        line = file.readline()
        # ajoute l'élément de la 1ère case au tableau qui contient la demande des clients
        demand.append(int(line.split()[0]))
        
        # création du tableau des coûts d'affectation du client j aux entrepôts
        cost =[]
        
        # lecture de la ligne suivante et séparation des éléments de la ligne
        # dans un tableau en utilisant l'espace comme séparateur
        line = file.readline()
        lineTab = line.split()

        for i in range(nb_warehouses):
            # ajout de l'élément de la case i au tableau contenant
            # les coûts d'affectation du client j aux entrepôts
            cost.append(float(lineTab[i])) 
        
        # ajout du tableau cost au tableau aux entrepôts au tableau
        # contenant les coûts d'affectations de tous les clients au dépôt
        assignment_cost.append(cost) 
        
# Affichage des informations lues
print("Nombre d'entrepôts = ", nb_warehouses)
print("Capacité des entrepôts = ", capacity)
print("Coût d'ouverture des entrepôts = ", opening_cost)
print("Nombre de clients = ", nb_customers)
print("Demande des clients = ", demand)
#for j in range(nb_customers):
#    print(assignment_cost[j])

# Import du paquet PythonMIP et de toutes ses fonctionnalités
from mip import *
# Import du paquet time pour calculer le temps de résolution
import time 

# Création du modèle vide 
model = Model(name = "CWFL", solver_name="CBC")  # Utilisation de CBC (remplacer par GUROBI pour utiliser cet autre solveur)

# Création des variables z et y
z = [model.add_var(name="z(" + str(i) + ")", lb=0, ub=1, var_type=BINARY) for i in range(nb_warehouses)]
y = [[model.add_var(name="y(" + str(j) + "," + str(i) + ")", lb=0, ub= 1, var_type=CONTINUOUS) for i in range(nb_warehouses)] for j in range(nb_customers)]

# Ajout de la fonction objectif au modèle
model.objective = minimize(xsum(opening_cost[i] * z[i] for i in range(nb_warehouses))+xsum(assignment_cost[j][i]*y[j][i] for j in range(nb_customers) for i in range(nb_warehouses)) )

# Ajout des contraintes au modèle
for j in range(nb_customers):  
    model.add_constr(xsum([y[j][i] for i in range(nb_warehouses)]) == 1)  # Contraintes (2)

for i in range(nb_warehouses):  
    model.add_constr(xsum([demand[j]*y[j][i] for j in range(nb_customers)]) <= capacity[i]*z[i])  # Contraintes (3)

# Ecrire le modèle (ATTENTION ici le modèle est très grand)
model.write("cwfl.lp") #à décommenter si vous le souhaitez

# Indication au solveur d'un critère d'optimalité : gap relatif en dessous duquel la résolution sera stoppée et la solution considérée comme optimale
model.max_mip_gap = 1e-6
# Indication au solveur d'un critère d'optimalité : gap absolu en dessous duquel la résolution sera stoppée et la solution considérée comme optimale 
model.max_mip_gap_abs = 1e-8

# Lancement du chronomètre
start = time.perf_counter()

# Résolution du modèle
status = model.optimize(max_seconds = 60)

# Arrêt du chronomètre et calcul du temps de résolution
runtime = time.perf_counter() - start

print("\n----------------------------------")
if status == OptimizationStatus.OPTIMAL:
    print("Status de la résolution: OPTIMAL")
elif status == OptimizationStatus.FEASIBLE:
    print("Status de la résolution: TEMPS LIMITE et UNE SOLUTION REALISABLE CALCULEE")
elif status == OptimizationStatus.NO_SOLUTION_FOUND:
    print("Status de la résolution: TEMPS LIMITE et AUCUNE SOLUTION CALCULEE")
elif status == OptimizationStatus.INFEASIBLE or status == OptimizationStatus.INT_INFEASIBLE:
    print("Status de la résolution: IRREALISABLE")
elif status == OptimizationStatus.UNBOUNDED:
    print("Status de la résolution: NON BORNE")
    
print("Temps de résolution (s) : ", runtime)
print("----------------------------------")

# Si le modèle a été résolu à l'optimalité ou si une solution a été trouvée dans le temps limite accordé
if model.num_solutions>0:
    print("Solution calculée")
    print("-> Valeur de la fonction objectif de la solution calculée : ",  model.objective_value)  # ne pas oublier d'arrondir si le coût doit être entier
    print("-> Meilleure borne inférieure sur la valeur de la fonction objectif = ", model.objective_bound)
    for i in range(nb_warehouses):
        if (z[i].x >= 0.5):
            print("- L'entrepôt ",i , " est ouvert [capacité = ", capacity[i], "] et les clients suivants lui sont affectés")
            for j in range(nb_customers):
                if (y[j][i].x >= 1e-4):
                    print("\t Client ",j, " pour ", round(y[j][i].x * 100,1), " % de sa demande -> ",round(y[j][i].x * demand[j],1))
else:
    print("Pas de solution calculée")
print("----------------------------------\n")

if model.num_solutions>0: # Si une solution a été calculée
    solutionfileName = 'solution_cap41.txt' #nom du fichier solution
    with open(solutionfileName, 'w') as file:  #ouvre le fichier, le ferme automatiquement à la fin et gère les exceptions
        file.write(str(model.objective_value)) #Il faut convertir les valeurs numériques en chaîne de caractères
        file.write("\n") #Je passe à la ligne suivante
        for i in range(nb_warehouses):
            if (z[i].x >= 0.5):
                file.write(str(i)) 
                file.write("\n") #Je passe à la ligne suivante
                for j in range(nb_customers):
                    if (y[j][i].x >= 1e-4):
                        file.write(str(j)+" "+str(round(y[j][i].x * 100,2)))
                        file.write("\n") #Je passe à la ligne suivante

