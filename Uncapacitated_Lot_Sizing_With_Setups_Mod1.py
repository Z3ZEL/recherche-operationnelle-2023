from tool.array_printer import TwoDimArray
import os
from math import *

datafileName = 'Instances_ULS/Toy_Instance.txt'

if(len(os.sys.argv)>1):
    datafileName = os.sys.argv[1]





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

# print(nbPeriodes)
# print(demandes)
# print(couts)
# print(cfixes)
# print(cstock)




from mip import *
import time

model = Model(name = "ULS", solver_name="CBC")
model.verbose = 0

y = [model.add_var(var_type=INTEGER, name="y_"+str(i),lb=0, ub=1) for i in range(nbPeriodes)]
x = [model.add_var(var_type=INTEGER, name="x_"+str(i),lb=0) for i in range(nbPeriodes)]
s = [model.add_var(var_type=INTEGER, name="s_"+str(i),lb=0) for i in range(nbPeriodes)]

M = sum(demandes)


model.objective = minimize( xsum( couts[i]*x[i] + cfixes[i]*y[i] + cstock*s[i] for i in range(nbPeriodes) ) )

for i in range(nbPeriodes):
    model.add_constr( x[i] <= M*y[i] , name="c1_"+str(i) )


model.add_constr( s[0] + demandes[0] == x[0]);


for i in range(1,nbPeriodes):
    model.add_constr( s[i] + demandes[i] == x[i] + s[i-1] , name="c2_"+str(i) )



#Commande pour recuperer les résultats après les avoirs enregistré dans un fichié
#find out_model1/ -type f -exec grep -a "Status" {} +
# model.write("test.lp")
linear_solution = 0;
print("| ", end="")

linear_status = model.optimize(max_seconds=180, relax=True)
if model.num_solutions>0:
    print(model.objective_value, end=" | ");
    linear_solution = model.objective_value;

start_time = time.time()

status = model.optimize(max_seconds=180)

delta = time.time() - start_time
delta = round(delta, 2)


def str_status(status):
    if status == OptimizationStatus.OPTIMAL:
        return "OPTIMAL"
    elif status == OptimizationStatus.FEASIBLE:
        return "FEASIBLE"
    elif status == OptimizationStatus.NO_SOLUTION_FOUND:
        return "NO_SOLUTION_FOUND"
    elif status == OptimizationStatus.INFEASIBLE:
        return "INFEASIBLE"
    elif status == OptimizationStatus.UNBOUNDED:
        return "UNBOUNDED"
    elif status == OptimizationStatus.NOT_SOLVED:
        return "NOT_SOLVED"
    elif status == OptimizationStatus.INFEASIBLE_OR_UNBOUNDED:
        return "INFEASIBLE_OR_UNBOUNDED"
    else:
        return "UNKNOWN"
                                
if model.num_solutions>0:
    print(str_status(model.status), end=" | ");
    print(model.objective_value, end=" | ");
    print(round((linear_solution/model.objective_value)*100), end=" | ");
    #NUMBER OF NODE IN THE BRANCH AND BOUND TREE
    print(model.max_nodes, end=" | ");
    print(delta, end=" |");
    #resolution time
    # print(model.solve_time, end=" | ");
    # print("-> Valeurs des variables de la solution calculée : ")
    # names = ["Période", "Demande", "Production", "Stock", "Production ?"]
    # array = [[i, demandes[i], x[i].x, s[i].x, "oui" if y[i].x == 1 else "non"] for i in range(nbPeriodes)]

    # print(TwoDimArray(array, names))
    
