#! usr/bin/python3
#! coding: utf-8

from extract_critique import getCritiques
from getInfos import getInfos
import io

if __name__ == '__main__':
	# fichier d'entrée de critiques au format XML
	filename = "Series_200_10.xml"
	# fichier de sortie au format tabulaire
	output = io.open("critiques.tab","w", encoding="utf8")
	# récupération des critiques à partir du fichier au format XML
	# le dictionaire "critiques" contient {id_critique:{'critique':'my_critique',note:my_note},id_critique: {...}} 
	critiques = getCritiques("../../Corpus/XML/"+filename)
	# récupération des informations de chaque critique
	# dictionnaire infos = infos = {id:[critique,note,présence nous,presence je,presence mais,presence alors_que,nombre mots]}
	infos = getInfos(critiques)
	# impression des éléments du dictionanire infos dans un fichier de sortie
	for element in infos:
		print(element)
		output.write("\""+infos[element][0]+"\"")
		# pour chaque information sur la critique, impression dans le fichier de sortie
		for i in range(1,len(infos[element])):
		# for info in infos[element]:
			# création du tabulaire 
			# output.write("\t")
			# critique	nous	mais	alors_que	nb_mots	nb_ponctuation	nb_point_interrogation	nb_virgule	note
			# les notes ont été simplifiées :
			# 1 pour les critiques ayant une note entre 1 et 4
			# 5 pour les notes entre 5 et 7
			# 10 pour les notes entre 8 et 10
			item = "\t" + str(infos[element][i])
			# write(u'android.library.reference.{}={}\n'.format(index + 1, ref))
			output.write(u'{}'.format(item))
		output.write(u"\n")
