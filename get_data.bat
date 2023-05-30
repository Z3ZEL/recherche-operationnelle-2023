@echo off

:: Chemin du dossier à parcourir
set "dossier=C:/Users/esteb/Documents/recherche-operationnelle-2023/Instances_ULS"

:: Parcours de tous les éléments dans le dossier
for %%F in ("%dossier%\*") do (
    :: Vérifier si l'élément est un fichier
    echo "Traitement du fichier %%F"
    :: Ptyhon script
    python Uncapacitated_Lot_Sizing_With_Setups_Mod2.py %%F > "C:/Users/esteb/Documents/recherche-operationnelle-2023/out_model2/%%~nF.txt"
)
