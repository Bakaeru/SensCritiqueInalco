# SensCritiqueInalco



## Scripts :



### Scripts Python

- main.py : nettoyage du corpus, création du tabulaire pour le corpus d'entrainement
- etiquetage.py :
- corpus_test.py : création et mise au format tabulaire du corpus de test
- extract_critique.py : récupération des critiques et passage du format xml au format tabulaire
- getInfos.py : récupération des informations sur les critiques (nombre de mots, nombre de points d'exclamation ...)
- nettoyage.py : scirpt pour le nettoyage du corpus (enlève les if(!), intègre des espaces avant et après les ponctuations ...)

### Pour Wapiti
- config.crf : ficheir de configuration pour wapiti, prend en compte les 9 features du modèle, décrits dans le fichier
- wapiti.sh : lancement de wapiti (entrainement et application du modèle)

### Pour l'évaluation
- conllEval.py : calcul rappel et précision pour chaque classe, avant de lal ancer, il faut supprimer la dernière ligne (une seule) du ficheir sortie.wap

## Requirements :
- **io** pour l'ouverture de fichiers pour gérer les encodages

## Features
- Présence de "nous"
- Présence du "je"
- Présence de "mais"
- Présence de "alors que"
- Nombre de mots
- Nombre d'éléments de ponctuation
- Nombre de points d'exclamation
- Nombre de virgules

## Notes :
Comme Loic avait extrait deux fichiers sur les séries l'un a été utilisé comme corpus d'entrainement et l'autre comme corpus de test.
