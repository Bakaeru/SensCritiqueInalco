#! usr/bin/python3
#! coding: utf-8

'''
évaluation d'un modèle wapiti
prend en entrée un fichier tabulaire de sortie de wapiti
le fichier d'entrée doit contenir :
	une colonne contenant les prédictions de wapiti
	la dernière colonne doit contenir le résultat attendu
affiche l'exactitude, le rappel et la précision pour chaque classe (positif, négatif, neutre)
'''

with open('sortie.wap', 'r') as f:
	total = 0
	diff=0
	nb_positif = 0
	nb_negatif = 0
	nb_neutre = 0
	vrai_positif = 0
	vrai_negatif = 0
	vrai_neutre = 0
	att_positif = 0
	att_neutre = 0
	att_negatif = 0
	for line in f.readlines():
		if line != "\n":
			# récupération du contenu de chaque colonne
			infos = line.strip('\n').split("\t")
			last = len(infos)
			# on s'intéresse aux 2 dernières colonnes
			# la dernière colonne contient la réponse attendue
			bonne_reponse = int(infos[last-2])
			# l'avant-dernière colonne contient la réponse prédite par le wapiti
			reponse = int(infos[last-1])
			# affichage des réponses attendues et prédites
			print("attendue\t{}\t{}\ttrouvée".format(bonne_reponse,reponse))
			
			# comptage du nombre de réponse par classe (positif/negatif/neutre)
			if bonne_reponse == 1:
				nb_negatif+=1
			if bonne_reponse == 10:
				nb_positif +=1
			if bonne_reponse == 5:
				nb_neutre +=1
			
			# comptage nb de critiques attribuées à chaque classe
			if reponse == 1:
				att_negatif+=1
			elif reponse == 10:
				att_positif +=1
			elif reponse == 5:
				att_neutre +=1

			# compter le nombre de critiques attribuées correctement à chaque classe
			if bonne_reponse == reponse:
				if reponse == 1:
					vrai_negatif +=1
				if reponse == 5:
					vrai_neutre+=1
				if reponse == 10:
					vrai_positif+=1

			# comptage du nombre de réponses fausses
			if bonne_reponse != reponse:
				# print("different {} != {}".format(bonne_reponse,reponse))
				diff+=1
			total +=1

print("fin de la lecture du fichier")

print("Réponses fausses : {}.".format(diff))
print("Nombres de critiques traitées : {}".format(total))
acc = float(diff)/float(total)*100
print("Exactitude : {}%".format(acc))

# rappel = doc corrects / doc appartenant à la classe
rappel_positif = float(vrai_positif)/float(nb_positif)
rappel_neutre = float(vrai_neutre)/float(nb_neutre)
rappel_negatif = float(vrai_negatif)/float(nb_negatif)

# precision = nb documents correct / nb documents attribués
precision_positif = float(vrai_positif)/float(att_positif)
precision_neutre = float(vrai_neutre)/float(att_neutre)
precision_negatif = float(vrai_negatif)/float(att_negatif)

print("\tPositifs\tNeutres\tNégatifs")
print("Rappel\t{}\t{}\t{}".format(rappel_positif,rappel_neutre,rappel_negatif))
print("Précision\t{}\t{}\t{}".format(precision_positif,precision_neutre,precision_negatif))
