#! usr/bin/python3
#! coding: utf-8

from ttagger import tag_critique
from extract_critique import getCritiques

def etiquetage(critiques):
	'''
	prend les clés d'un dictionnaire et les étiquette avec treetagger
	'''
	infos = {}
	for element in critiques:
		tags = tag_critique(element)
		infos[element] = tags
	return infos

if __name__ == '__main__':
	filename = "Series_200_10.xml"
	# dictionaire critiques contient {note:texte de la critique}
	critiques = getCritiques("../../Corpus/XML/"+filename)
	# etiquetage
	etiquetage(critiques)