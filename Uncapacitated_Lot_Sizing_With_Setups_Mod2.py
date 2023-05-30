
datafileName = 'Instances_ULS/Toy_Instance.txt'

from tool.array_printer import TwoDimArray

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

#print(nbPeriodes)
#print(demandes)
#print(couts)
#print(cfixes)
#print(cstock)

from mip import *
import time


model2 = Model(name = "ULS", solver_name="CBC")

y = [model2.add_var(var_type=mip.BINARY, name="y_"+str(i)) for i in range(nbPeriodes)]
x = [[model2.add_var(var_type=mip.BINARY, name="x_"+str(i)+"_"+str(j)) for i in range(j+1) ] for j in range(nbPeriodes)]

model2.objective = minimize(
    xsum(
        xsum( x[j][i]*demandes[j]*couts[i] for i in range(j+1) ) 
        for j in range(nbPeriodes)
        )
+ cstock*xsum(
    xsum(x[j][i]*demandes[j]*(j-i)  for i in range(j+1)) 
    for j in range(nbPeriodes)
    )
+ xsum(
    cfixes[i]*y[i] for i in range(nbPeriodes) 
    ) 
    )

for j in range(nbPeriodes):
    model2.add_constr( xsum( (x[j][i] ) for i in range(j+1) ) == 1 )

M = nbPeriodes

for i in range(nbPeriodes):
    model2.add_constr( xsum( (x[j][i] ) for j in range(i,nbPeriodes) ) <= M*y[i] )





#model2.write("test.lp")

status = model2.optimize()

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

if model2.num_solutions>0:
    print("Solution calculée")
    print("-> Valeur de la fonction objectif de la solution calculée : ",  model2.objective_value)
    #show x i,j
    # print("-> Valeur des variables x i,j de la solution calculée : ")

    x_value = [[str(i) +' -> ' +str(j) if x[j][i].x == 1 else "X"  for i in range(j+1)] for j in range(nbPeriodes)]
    printer = TwoDimArray(x_value,[str(i) for i in range(nbPeriodes)])
    print(printer)

    #show y i
    # print("-> Valeur des variables y i de la solution calculée : ")






