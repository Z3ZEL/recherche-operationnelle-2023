# Comparaison de formulations pour le problème de Lot-Sizing sans capactié avec setups

- [Comparaison de formulations pour le problème de Lot-Sizing sans capactié avec setups](#comparaison-de-formulations-pour-le-problème-de-lot-sizing-sans-capactié-avec-setups)
  - [Introduction](#introduction)
  - [Les modèles](#les-modèles)
    - [Premier modèle](#premier-modèle)
    - [Deuxième modèle](#deuxième-modèle)
  - [Résultats](#résultats)
    - [Premier modèle](#premier-modèle-1)
    - [Deuxième modèle](#deuxième-modèle-1)
  - [Analyse](#analyse)
  - [Conclusion](#conclusion)


## Introduction


## Les modèles
### Premier modèle
  En partant de l'énnoncé du problème, et des variables suivantes :
  - $x_{i}$ : quantité produite à la période $i$
  - $y_{i}$ : {0,1} si une production est effectuée à la période $i$ (1 si on produit, 0 sinon)
  - $s_{i}$ : quantité stockée à la fin du mois $i$
  avec $i \in \{0,..., n\}$

  Nous pouvons écrire le modèle PLNE suivant :

  $$
    min \sum_{i=1}^{n} (c_{i}x_{i} + hs_{i} + f_iy_{i}) \\
    s.c. \space\space x_i \leq M y_i, \space\space \forall i \in \{0,...,n\} \\
    s_i + d_i = x_i + s_{i-1}, \space\space \forall i \in \{1,...,n\} \\
    s_0 + d_0 = x_0 \\
  $$

  avec $M$ une constante suffisament grande pour que $x_i \leq M y_i$ soit toujours vérifié. Par exemple ici nous avons pris $M = \sum{d_i}$.

  de plus nous introduisons les variables suivantes :

  - $c_{i}$ : coût de production à la période $i$
  - $h$ : coût de stockage (fixe)
  - $f_{i}$ : coût de mise en marche de la machine à la période $i$




### Deuxième modèle

## Résultats

### Premier modèle

Nous avons appliqué le modèle à plusieurs instances de test, et nous avons obtenu les résultats suivants :

```
Instance120.10 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  87317.0
Instance120.1 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  81016.0
Instance120.2 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  68779.0
Instance120.3 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  91756.0
Instance120.4 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  86080.0
Instance120.5 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  98123.0
Instance120.6 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  65754.0
Instance120.7 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  82356.0
Instance120.8 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  74145.0
Instance120.9 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  88495.0
Instance21.1 OPTIMAL ->  13068.0
Instance60.10 OPTIMAL ->  31809.0
Instance60.1 OPTIMAL ->  29739.0
Instance60.2 OPTIMAL ->  27572.0
Instance60.3 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  34081.0
Instance60.4 OPTIMAL ->  31131.0
Instance60.5 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  35693.0
Instance60.6 OPTIMAL ->  25186.0
Instance60.7 OPTIMAL ->  30853.0
Instance60.8 OPTIMAL ->  27962.0
Instance60.9 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  35492.0
Instance90.10 TEMPS LIMITE et SOLUTION REALISABLE CALCULEE ->  57878.0
Instance90.1 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  51363.0
Instance90.2 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  46826.0
Instance90.3 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  57613.0
Instance90.4 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  53897.0
Instance90.5 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  64943.0
Instance90.6 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  42086.0
Instance90.7 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  54913.0
Instance90.8 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  49063.0
Instance90.9 TEMPS LIMITE et SOLUTION REALISABLE CALCULE ->  59618.0
Toy_Instance OPTIMAL->  1788.0
```
Nous avons récolté les résultats pour chacunes des variables, nous pouvons détailler celle de *Toy_Instance* :

```
Période      Demande      Production   Stock        Production ?
-----------------------------------------------------------------
0            30           70.0         40.0         oui
1            25           0.0          15.0         non
2            15           0.0          0.0          non
3            47           106.0        59.0         oui
4            34           0.0          25.0         non
5            10           0.0          15.0         non
6            15           0.0          0.0          non
```
> Résultat détaillé de l'instance : `Toy_Instance.txt`



### Deuxième modèle

## Analyse

## Conclusion

