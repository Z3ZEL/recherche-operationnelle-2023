import os
datafileName = 'Instances_ULS/Toy_Instance.txt'

if(len(os.sys.argv)>1):
    datafileName = os.sys.argv[1]




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
model2.verbose = 0
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
linear_solution = 0;
print("| ", end="")

linear_status = model2.optimize(max_seconds=180, relax=True)
if model2.num_solutions>0:
    print(model2.objective_value, end=" | ");
    linear_solution = model2.objective_value;

start_time = time.time()

status = model2.optimize(max_seconds=180)

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
                                
if model2.num_solutions>0:
    print(str_status(model2.status), end=" | ");
    print(model2.objective_value, end=" | ");
    print(round((linear_solution/model2.objective_value)*100), end=" | ");
    #NUMBER OF NODE IN THE BRANCH AND BOUND TREE
    print(model2.max_nodes, end=" | ");
    print(delta, end=" |");





