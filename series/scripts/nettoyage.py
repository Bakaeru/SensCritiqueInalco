#! usr/bin/python3
#! coding: utf-8

import re

def nettoyage(string):
	"""
	"""
	string = re.sub("undef", "", string)
	string = re.sub(r"[{}'\"=]", " ", string)
	string = re.sub(r"\n|\t", "", string)
	string = re.sub(r"  ", "", string)
	string = re.sub(r"!", ". ", string)
	string = re.sub(r"\.", " . ", string)
	string = re.sub(r"!", " ! ", string)
	string = re.sub(r",", " , ", string)
	string = re.sub(r"\?", " . ", string)
	string = re.sub(r"( if )|(render)|(undef)|(typeof)|(sas)|(ined)", "", string)
	return string

if __name__ == '__main__':
	texte = "Avis à ceux qui déteste la société actuelle : Regardez cette série sans hésitation !\nMr. \n				if (typeof sas !== 'undefined') {\n					sas.render('41614');\n				}\n			Robot nous plonge dans un univers un peu à la Fight Club, avec une touche de Kubrick, des frères Cohen, et pleins de petits clins d’œil à plusieurs films, séries etc."
	texte = nettoyage(texte)
	print(texte)