from traitement_fic_xml import *
from traitement_fic_json import *
from traitement_fic_svg import *
from validation import *
import xml.etree.ElementTree as ET
tableau_nom_association=[]
tableau_nom_entite=[]
tableau_attribut_interne=[]
tableau_attributs_association=[]
tableau_attributs_entite=[]
print('Taper la commande sous la forme:XJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg')
commande=get_commande()
if commande=='help' or commande == '?':
	print ('Available commande:\n about')
	print (' help')
	print (' ?')
	print (' quit')
	print (' XJ_Convertor[-i -t -f -o]')
	print ('tape help [commande] for more helps. Ex: help XJ_Convertor')
if commande == 'about' or commande=='a':
	print ('Reverse Engineering')
if commande =='quit' or commande == 'q':
	exit(0)

else:
	liste=split_commande(commande)
	test_input_file(liste)
	test_output_file(liste)
	test_commande(liste)
if test_output_file(liste)==True and test_input_file(liste)==True and test_commande(liste)==True:
	if len(liste)==7:
		if(liste[2]=="xml"):
			if liste[3]=="-f":
				root = get_root(ET,liste[4])
			else:
				d=split_url(liste[4])
				root = get_root(ET,d)
			get_entity_name(root,tableau_nom_entite,tableau_nom_association,tableau_attribut_interne)
			get_attribs(root,tableau_attributs_entite,tableau_attributs_association,tableau_nom_entite,tableau_nom_association)
		else:
			traite_json(tableau_attributs_entite,tableau_attributs_association,tableau_nom_entite,tableau_nom_association)	
		dwg=background(liste[6])
		create_entity(tableau_nom_entite,tableau_nom_association,dwg,tableau_attributs_entite,tableau_attributs_association)
	if len(liste)==8:
		if(liste[2]=="xml"):
			root = get_root(ET,liste[5])
			get_entity_name(root,tableau_nom_entite,tableau_nom_association,tableau_attribut_interne)
			get_attribs(root,tableau_attributs_entite,tableau_attributs_association,tableau_nom_entite,tableau_nom_association)
		else:
			traite_json(tableau_attributs_entite,tableau_attributs_association,tableau_nom_entite,tableau_nom_association)
		dwg=background(liste[6])
		create_entity(tableau_nom_entite,tableau_nom_association,dwg,tableau_attributs_entite,tableau_attributs_association)
		trace(tableau_attributs_entite,tableau_attributs_association,tableau_nom_entite,tableau_nom_association)
	print ("Fichier "+liste[len(liste)-1]+" bien genere, consulter le repertoire courant")
	dwg.save()