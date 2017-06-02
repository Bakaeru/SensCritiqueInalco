#! usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
from nettoyage import nettoyage
from getInfos import getInfos
import io

def extract_corpus_test(input_file):
	dic={}
	tree = ET.parse(input_file)
	corpus = tree.getroot()
	j=0
	for oeuvre in corpus:
		i = 0
		for critique in list(oeuvre):
			id_critique = str(i)+'-'+str(j)
			dic[id_critique] = {}
			texte_critique = critique.text
			texte_critique = nettoyage(texte_critique)
			note = critique.attrib["note"]
			dic[id_critique]['critique'] = texte_critique
			dic[id_critique]['note'] = note
			i+=1
		j+=2
	return dic
	
if __name__ == '__main__':
	filename = "Series_200_20.xml"
	input_file = extract_corpus_test("../../Corpus/XML/"+filename)
	infos = getInfos(input_file)
	output = io.open("corpus_test.tab","w", encoding="utf8")
	for element in infos:
		output.write(infos[element][0])
		for i in range(1,len(infos[element])):
		# for info in infos[element]:
			# création du tabulaire 
			output.write("\t")
			# critique	nous	mais	alors_que	nb_mots	nb_ponctuation	nb_point_interrogation	nb_virgule	note
			# les notes ont été simplifiées :
			# 1 pour les critiques ayant une note entre 1 et 4
			# 5 pour les notes entre 5 et 7
			# 10 pour les notes entre 8 et 10
			output.write(str(infos[element][i]))
		output.write("\n")
