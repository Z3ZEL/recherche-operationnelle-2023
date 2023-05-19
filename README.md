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

