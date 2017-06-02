#!/bin/sh

# il faut avoir créé les corpus de train et de test donc les scripts suivants :
# python3 main.py
# python3 corpus_test.py

# création du modèle
wapiti train -a rprop -p config.crf critiques.tab modele.wap

# application du modèle
wapiti label -m modele.wap -p corpus_test.tab > sortie.wap

# pour avoir une évaluation des résultats
# python3 conllEval.py