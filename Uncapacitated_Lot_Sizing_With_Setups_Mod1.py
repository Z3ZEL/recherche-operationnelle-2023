

datafileName = 'Instances_ULS/Toy_Instance.txt'

with open(datafileName, "r") as file:
    line = file.readline()
    lineTab = line.split()
    nbPeriodes = int(lineTab[0])

    line = file.readline()
    lineTab = line.split()
    demandes = []
    for i in range(nbPeriodes):
        demandes.append(int(lineTab[i]))

    line = file.readline()
    lineTab = line.split()
    couts = []
    for i in range(nbPeriodes):
        couts.append(int(lineTab[i]))

    line = file.readline()
    lineTab = line.split()
    cfixes = []
    for i in range(nbPeriodes):
        cfixes.append(int(lineTab[i]))

    line = file.readline()
    lineTab = line.split()
    cstock = int(lineTab[0])

print(nbPeriodes)
print(demandes)
print(couts)
print(cfixes)
print(cstock)




from mip import *
import time

model = Model(name = "ULS", solver_name="CBC")

y = [model.add_var(var_type=INTEGER, name="y_"+str(i),lb=0, ub=1) for i in range(nbPeriodes)]
x = [model.add_var(var_type=INTEGER, name="x_"+str(i),lb=0) for i in range(nbPeriodes)]
s = [model.add_var(var_type=INTEGER, name="s_"+str(i),lb=0) for i in range(nbPeriodes)]

M = max(demandes)
print("Max de la demande : " + str(M))


model.objective = minimize( xsum( couts[i]*x[i] for i in range(nbPeriodes) ) + xsum( y[i]*cfixes[i] for i in range(nbPeriodes) ) + xsum( cstock*s[i] for i in range(nbPeriodes) ) )

for i in range(nbPeriodes):
    model.add_constr( x[i] + s[i] >= demandes[i], name="c1_"+str(i) )
    model.add_constr( x[i] <= M*y[i], name="c2_"+str(i) )
    # model.add_constr( s[i] <= M*(1-y[i]), name="c3_"+str(i) )


model.add_constr( x[0] <= M*y[0], name="c4_"+str(0) )
model.add_constr( s[0] <= 0, name="c5_"+str(0) )
for i in range(1,nbPeriodes):
    # model.add_constr( s[i] == (s[i-1] + x[i-1]) - demandes[i-1] + (x[i]-demandes[i]), name="c5_"+str(i) )
    # model.add_constr( s[i] == x[i] - demandes[i], name="c5_"+str(i) )
    model.add_constr( xsum( x[i] + s[i] for i in range(i) ) >= xsum( demandes[i] for i in range(i) ), name="c5_"+str(i) )







# model.write("test.lp")

status = model.optimize()

print("\n----------------------------------")
if status == OptimizationStatus.OPTIMAL:
    print("Status de la résolution: OPTIMAL")
elif status == OptimizationStatus.FEASIBLE:
    print("Status de la résolution: TEMPS LIMITE et SOLUTION REALISABLE CALCULEE")
elif status == OptimizationStatus.NO_SOLUTION_FOUND:
    print("Status de la résolution: TEMPS LIMITE et AUCUNE SOLUTION CALCULEE")
elif status == OptimizationStatus.INFEASIBLE or status == OptimizationStatus.INT_INFEASIBLE:
    print("Status de la résolution: IRREALISABLE")
elif status == OptimizationStatus.UNBOUNDED:
    print("Status de la résolution: NON BORNE")

if model.num_solutions>0:
    print("Solution calculée")
    print("-> Valeur de la fonction objectif de la solution calculée : ",  model.objective_value)

    print("-> Valeurs des variables de la solution calculée : ")
    print("| Periode | Demande | Production | Stock | Production ? |")
    for i in range(nbPeriodes):
        print("| " + str(i) + "     | " + str(demandes[i]) + "       | " + str(x[i].x) + "       | " + str(s[i].x) + "      | " + str( "oui" if y[i].x == 1 else "non" ) + "       |")
        

