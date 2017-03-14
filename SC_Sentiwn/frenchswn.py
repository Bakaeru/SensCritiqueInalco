#! /usr/bin/python3
#! coding: utf-8

from pprint import pprint
import xml.etree.ElementTree as ET

def traitement_dicSWNFrench(frenchWN):
	"""
	parse le xml avec les donnees fr
	renvoie un dictionnaire {iD -> [liste de termes fr]}
	"""
	dico={}
	#initialisation du dictionnaire final
	tree=ET.parse(frenchWN)
	root= tree.getroot()
	# Parcours du xml parse
	for child in root:
		for subnode in child:
			#recuperation de l'identifiant
			if subnode.tag =="ID":
				# passage du format 'eng-30-00218330-v' a '00218330'
				# pour matcher SWNEnglish
				iD=subnode.text.split('-')[2]
				#creation de l'entree de dictionnaire
				dico[iD]={}
			#recuperation des termes
			if subnode.tag == "SYNONYM":
				#creation de la sous entree "word" 
				#(plus pratique pour associer les dictionnaires)
				dico[iD].update({"word":[]})
				for elem in subnode.iter():
					if elem.tag == 'LITERAL':
						#remplissage du dictionnaire
						dico[iD]["word"]+=[elem.text]
	return dico

def traitement_dicSWNEnglish(engSWN):
	"""
	parcours le tabulaire et extrait les donnees
	renvoie un dic { iD ->
				{
				'NegScore' -> str entre 0 et 1,
				'PosScore' -> str entre 0 et 1,
				'SynsetTerms' -> str termes separes par espaces
				}
			}
	"""
	f=open(engSWN)
	# initialisation du dico final
	dicodata={}
	#parcours du fichier
	for line in f.readlines():
		#exclusion des commentaires
		if not line.startswith("#"):
			#on split sur le separateur
			data=line.split("\t")
			#on recupere seulement ce qui nous interesse
			dicodata[data[1]]={"PosScore":data[2],"NegScore":data[3], "SynsetTerms": data[4]}
	f.close()
	return dicodata


def upgradeDico(engSWN, frenchWN):
	"""
	association des dictionnaires fr et en en fonction de iD
	entree : engSWN str nom de fichier en
	frenchWN str nom de fichier fr
	"""
	#creation des dictionnaires
	engdico=traitement_dicSWNEnglish(engSWN)
	frenchdico=traitement_dicSWNFrench(frenchWN)
	# initialisation du dico final
	finaldic={}
	#on croise des sets des entrees des deux dicos 
	# permet de gagner du temps pour les parcourir
	#(merci SO !)
	dc = set(engdico) & set(frenchdico)
	#pour chaque iD
	for i in dc:
		#on augmente le dico en avec les data fr
		engdico[i].update(frenchdico[i])
		#on fait une copie
		finaldic[i]=engdico[i] 
	return finaldic

def writeFinalFile(finaldic, outfilename):
	"""
	Ecriture du fichier de sortie
	prend le dico final et une str de nom de fichier
	"""
	#ouverture du fichier 
	# TODO : prevoir plusieurs formats de sortie
	f = open(outfilename,"w")
	#ecriture des noms de colonnes
	f.write('\t'.join(['FrenchWord','EnglishTerms','NegScore','PosScore'])+'\n')
	# parcours du dico final
	for iD in sorted(finaldic):
		frw = "#".join(finaldic[iD]["word"])
		enSt = finaldic[iD]["SynsetTerms"]
		negscore=finaldic[iD]['NegScore']
		poscore=finaldic[iD]['PosScore']
		engw=""
		# Traitement des termes eng
		# passage du format 'prescriptive#1 normative#2' a 'prescriptive normative'
		if ' ' in enSt:
			engl=enSt.split(' ')
			engw=" ".join([w.split("#")[0] for w in engl])
			# print(engw)
			# ljbk
		else:
			engw=enSt.split("#")[0]
		f.write("\t".join([frw, engw, negscore, poscore])+'\n')
	f.close()




if __name__ == '__main__':
	finaldic=upgradeDico("EngData/SentiWordNet_3.0.0_20130122.txt","FrData/wonef-fscore-0.1.xml")
	writeFinalFile(finaldic,"FrenchSentiWordnet.tab")