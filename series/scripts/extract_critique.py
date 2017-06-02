#! usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
from nettoyage import nettoyage
from pprint import pprint

def getCritiques(infilename):
	"""
	extraits les critiques et la note correspondante
	renvoi un dictionnaire : {id_critique:{'critique':'my_critique',note:my_note},id_critique: {...}} 
	"""
	dic={}
	tree = ET.parse(infilename)
	corpus = tree.getroot()
	j=0
	for oeuvre in corpus:
		i = 0
		for critique in list(oeuvre):
			# création d'un id pour chaque critique
			id_critique = str(i)+'-'+str(j)
			dic[id_critique] = {}
			texte_critique = critique.text
			# nettoyage du texte
			texte_critique = nettoyage(texte_critique)
			# récupération de la note associée à la critique
			note = critique.attrib["note"]
			dic[id_critique]['critique'] = texte_critique
			dic[id_critique]['note'] = note
			i+=1
		j+=2
	return dic

if __name__ == '__main__':
	filename = "Series_200_10.xml"
	critiques = getCritiques("../../Corpus/XML/"+filename)
	pprint(critiques)