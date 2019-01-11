#Traitement du fichier XML
import random
import string
#fonction qui recupere la racine du fichier xml
def get_root(ET,doc_xml):
	tree = ET.parse(doc_xml)
	root = tree.getroot()
	return root
# Fonction qui recupere des attributs contenus au niveau des balises
def recup_atrib_interne(elem):
	a=[]
	params = elem.attrib
	chaine= ",".join(["%s=%s" % (k, v) for k, v in params.items()])
	liste = chaine.split(",")
	for i in xrange(0,len(liste)):
		chaine1=liste[i].split("=")
		if chaine1[0]!='':
			a.append(chaine1[0])
	return a
# Fonction qui recuper les noms des entites
def get_entity_name(root,tableau_nom_entite,tableau_nom_association,tableau_attribut_interne):
	for child in root:
		a=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
		a=recup_atrib_interne(child)
		if (a[0] in tableau_attribut_interne)==True and (child.tag in tableau_nom_entite) == False:
			if (child.tag in tableau_nom_association)==False:
				tableau_nom_association.append(child.tag)
		if(child.tag in tableau_nom_association)==False:
			if (child.tag in tableau_nom_entite) == False:
				tableau_nom_entite.append(child.tag)
				tableau_attribut_interne.append(a[0])
# Fonction qui recupere les attributs
def get_attribs(root,tableau_attributs_entite,tableau_attributs_association,tableau_nom_entite,tableau_nom_association):
	nom=[]
	association=[]
	for child in root:
		if (child.tag in nom)==False and (child.tag in association)==False:
			if (child.tag in tableau_nom_entite)==True:
				a=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
				a=recup_atrib_interne(child)
				for child_child in child:
					a.append(child_child.tag)
				tableau_attributs_entite.append(a)
				nom.append(child.tag)
				
			if (child.tag in tableau_nom_association)==True:
				b=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
				b=[]
				for child_child in child:
					b.append(child_child.tag)
				tableau_attributs_association.append(b)
				association.append(child.tag)
# Fonction qui permet de faire la trace 
def trace(tableau_attributs_entite,tableau_attributs_association,tableau_nom_entite,tableau_nom_association):
	for x in xrange(0,len(tableau_nom_entite)):
		print("Nom de l'entite: "+tableau_nom_entite[x]+":")
		print("	Attributs ("+str((len(tableau_attributs_entite[x])))+")")
		for i in xrange(0,len(tableau_attributs_entite[x])):
			if i==0:
				print("		-"+tableau_attributs_entite[x][i]+" (attribut principal)")
			else:
				print("		-"+tableau_attributs_entite[x][i])
		print ("")
		for i in xrange(0,len(tableau_attributs_association)):
			print ("Nom de l'association: "+str(tableau_nom_association[i]))
			print("	Attributs ("+str(len(tableau_attributs_association[i]))+")")
			for j in xrange(0,len(tableau_attributs_association[i])):
				print("		-"+tableau_attributs_association[i][j])