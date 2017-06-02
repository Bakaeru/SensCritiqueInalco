#! usr/bin/python3
#! coding: utf-8


def getInfos(critiques):
	"""
	fonction qui récupère les informations sur une critique (présence du nous, je , mais, alors_que, nombre de mot, ponctuations)
	renvoie un dictionnaire : infos = {id_critique:[critique,note,présence nous,presence je,presence mais,presence alors_que,nombre mots, ponctuation, presence musique]}
	"""
	infos = {}
	for id_critique in critiques:
		note = float(critiques[id_critique]['note'])
		infos[id_critique] = []
		text = critiques[id_critique]['critique']
		infos[id_critique].append(text)
		words = text.split(" ")
		# présence de "nous"
		if "nous" in words:
			infos[id_critique].append("nous")
		else:
			infos[id_critique].append("O")
		# présence de "je"
		if "je" in words:
			infos[id_critique].append("je")
		else:
			infos[id_critique].append("O")
		# présence du "mais"
		if "mais" in words:
			infos[id_critique].append("mais")
		else:
			infos[id_critique].append("O")
		# présence de "alors_que"
		if "alors" in words:
			index = words.index("alors")
			if words[index+1] == "que":
				infos[id_critique].append("alors_que")
		else:
			infos[id_critique].append("O")
		# prise en compte du nombre de mots dans la critique
		infos[id_critique].append(len(words))
		# comptage de la ponctuation
		ponct = 0
		# comptage des points
		for word in words:
			if word == ".":
				ponct+=1
		infos[id_critique].append(str(ponct))
		# comptage des points d'exclamation
		pint = 0
		for word in words:
			if word == "!":
				pint+=1
		infos[id_critique].append(str(pint))
		# comptage du nombre de virgule
		pvir = 0
		for word in words:
			if word == ",":
				pvir+=1
		infos[id_critique].append(str(pvir))
		# prise en compte de la présence de "musique"
		if "musique" in words:
			infos[id_critique].append("musique")
		else:
			infos[id_critique].append("O")
		# simplification des notes
		if note <= 4:
			# 1 si 1<note<=4
			infos[id_critique].append(1)
		elif 4 < note < 7:
			# 5 si 5<=note<7
			infos[id_critique].append(5)
		elif note >= 8:
			# 10 si 8<=note<=10
			infos[id_critique].append(10)
		else:
			# sinon on attribue la note 5 par défaut
			infos[id_critique].append(5)


	return infos
