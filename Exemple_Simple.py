from mip import *

# Création du modèle vide 
model = Model(name = "PLsimple", solver_name="CBC")

x = model.add_var(name="x", lb=0, ub=3, var_type=CONTINUOUS)
y = model.add_var(name="y", lb=0, var_type=CONTINUOUS)

model.objective = minimize(-3*x+y)

model.add_constr(x + y == 2, name="c1")

model.write("exemple.lp")

satus = model.optimize(max_seconds=120)

print("Valeur de la fonction objectif ", model.objective_value)
print("x = ", x.x, " y = ", y.x)
