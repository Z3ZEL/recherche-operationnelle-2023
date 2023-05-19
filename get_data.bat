@echo off

:: Chemin du dossier à parcourir
set "dossier=C:/Users/esteb/Documents/recherche-operationnelle-2023/Instances_ULS"

:: Parcours de tous les éléments dans le dossier
for %%F in ("%dossier%\*") do (
    :: Vérifier si l'élément est un fichier
    echo "Traitement du fichier %%F"
    python Uncapacitated_Lot_Sizing_With_Setups_Mod1.py %%F > "C:/Users/esteb/Documents/recherche-operationnelle-2023/out/%%~nF_out.txt"

    timeout /t 180 > nul

    :: Vérifier si le processus python est toujours en cours d'exécution
    tasklist /FI "PID eq %ERRORLEVEL%" 2>nul | find /i "python_script.py" >nul
    if %errorlevel% equ 1 (
        :: Le processus est terminé ou l'exécution a dépassé 3 minutes
        echo L'exécution du script pour %%F a été arrêtée car cela a pris plus de 3 minutes. >> "%fichier_sortie%"
    )
)
