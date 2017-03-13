# French SentiWordnet

Croisement de SentiWordNet (en anglais) avec FrenchWordNet

Cree un fichier tabulaire avec les colonnes suivantes :
	- FrenchWord : mot(s) français, souvent "_EMPTY_"
	- EnglishTerms : équivalent(s) anglais, toujours utile
	- NegScore : 0 <= score negatif <= 1
	- PosScore : 0 <= score positif <= 1

Utilisation : 
> python3 frenchswn.py

Fichier sorti :
FrenchSentiWordnet.tab

(les arguments peuvent être modifiés dans le main)

Sources : 
- English SentiWordNet : [http://sentiwordnet.isti.cnr.it/](http://sentiwordnet.isti.cnr.it/)
- FrenchWordnet : [https://wonef.fr/](https://wonef.fr/)

