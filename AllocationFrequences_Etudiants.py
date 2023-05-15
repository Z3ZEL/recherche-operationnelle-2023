datafileName = 'Instances_AllocFreq_Small/toy_instance.1.dat'

#ouverture du fichier, le ferme automatiquement à la fin et gère les exceptions
with open(datafileName, "r") as file:
    # lecture de la 1ère ligne et séparation des éléments de la ligne
    # dans un tableau en utilisant l'espace comme séparateur
    line = file.readline()  
    lineTab = line.split()
    
    # la valeur de la 1ère case correspond au nombre d'antennes
    # (attention de penser à convertir la chaîne de caractère en un entier)
    nbNodes = int(lineTab[0])

    # la valeur de la 2ème case correspond au nombre de conflits
    nbEdges = int(lineTab[1])

    # création d'un tableau qui stockera les capacités des entrepôts
    edges = []
    
    # pour chaque ligne contenant les informations sur les arêtes
    for i in range(nbEdges):
        # lecture de la ligne suivante et séparation des éléments de la ligne
        # dans un tableau en utilisant l'espace comme séparateur
        line = file.readline()
        lineTab = line.split()
        
        # ajout de l'arête sous forme de tableau avec deux éléments.
        # On diminue les numéros de noeuds de 1 pour coller avec les indices allant de 0 à n-1
        edges.append([int(lineTab[0])-1,int(lineTab[1])-1]) 
            

# Affichage du graphe
print("Nombre de sommets : ", nbNodes)
print("Liste des arêtes :")
for i in range(nbEdges):
    print(edges[i][0],"--",edges[i][1], "  ")


from mip import *

#Entrez votre premier modèle ici.

m1 = Model(name="First", solver_name="CBC")







m1.optimize()

print("Objective value : ", m1.objective_value)

