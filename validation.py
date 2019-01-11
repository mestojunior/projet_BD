#definition des fonctions qui traite la commande
#Fonction qui recupere la commande saisie
def get_commande():
	commande = input('>>>')
	return commande
#Fonction qui transforme en tableau la commande
def split_commande(commande):
		liste=commande.split(" ")
		return liste
#Fonction qui traite l'url
def split_url(url):
	extension = url.split("/")
	l=len(extension)
	fic=extension[l-1]
	return fic
#fonction qui traite le fichier d'entree
def test_input_file(liste):
	if len(liste)>2:
		if liste[2] == 'xml':
			if len(liste)==8:
				if liste[4]=='-f':
					extension = liste[5].split(".")
					#print(extension[0],extension[1])
					if len(extension)==2:
						if extension[1] != 'xml':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						return False
				if liste[4]=='-h':
					extension = liste[5].split("/")
					l=len(extension)
					fic=extension[l-1]
					fic1=fic.split('.')
					if len(fic1)==2:
						if fic1[1] != 'xml':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
			if len(liste)==7:
				if liste[3]=='-f':
					extension = liste[4].split(".")
				#print(extension[0],extension[1])
					if len(extension)==2:
						if extension[1] != 'xml':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
				if liste[3]=='-h':
					extension = liste[4].split("/")
					l=len(extension)
					fic=extension[l-1]
					fic1=fic.split('.')
					if len(fic1)==2:
						if fic1[1] != 'xml':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
		if liste[2] == 'json':
			if len(liste)==8:
				if liste[4]=='-f':
					extension = liste[5].split(".")
					#print(extension[0],extension[1])
					if len(extension)==2:
						if extension[1] != 'json':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						return False
				if liste[4]=='-h':
					extension = liste[5].split("/")
					l=len(extension)
					fic=extension[l-1]
					fic1=fic.split('.')
					if len(fic1)==2:
						if fic1[1] != 'json':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
			if len(liste)==7:
				if liste[3]=='-f':
					extension = liste[4].split(".")
				#print(extension[0],extension[1])
					if len(extension)==2:
						if extension[1] != 'json':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
				if liste[3]=='-h':
					extension = liste[4].split("/")
					l=len(extension)
					fic=extension[l-1]
					fic1=fic.split('.')
					if len(fic1)==2:
						if fic1[1] != 'json':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
		else:
			print('Erreur fichier d\'entree')
			return False
#Fonction qui traite le fichier de sortie
def test_output_file(liste):
	if len(liste)==7 or len(liste)==8:
		extension=liste[len(liste)-1].split(".")
		if len(extension)==2:
			if extension[1]=='svg':
				return True
			else:
				print('Erreur fichier de sortie:format svg attendu or format '+extension[1]+' entree')
				return False
		else:
			print('Erreur fichier de sortie')
			return False
#fonction qui traite le syntaxe de la commande
def test_commande(liste):
	if len(liste) == 8:
		if liste[0]=='XJ_Convertor':
		 	if liste[1]=='-i':
		 		if liste[3]=='-t':
		 			if liste[4]=='-f' or liste[4]=='-h':
		 				if liste[6]=='-o':
		 					return True
		 				else:
		 					print 'Erreur commande'
		 					return False
		 			else:
		 				print 'Erreur commande'
		 				return False
		 		else:
		 			print 'Erreur commande'
		 			return False
		 	else:
		 		print 'Erreur commande'
		 		return False
		else:
			print 'Erreur commande'
		 	return False
	if len(liste)==7:
		if liste[0]=='XJ_Convertor':
		 	if liste[1]=='-i':
		 		if liste[3]=='-f' or liste[3]=='-h':
		 			if liste[5]=='-o':
		 				return True
		 			else:
		 				print 'Erreur commande'
		 				return False
		 		else:
		 			print 'Erreur commande'
		 			return False
		 	else:
		 		print 'Erreur commande'
		 		return False
		else:
			print 'Erreur commande'
		 	return False
	else:
		print 'Erreur commande'
		return False