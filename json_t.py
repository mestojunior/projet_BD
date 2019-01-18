#Fonction qui traite le fichier json
def traite_json(tableau_attributs_entite,tableau_attributs_association,tableau_nom_entite,tableau_nom_association):
	tableau_nom_entite.append("Client")
	tableau_nom_entite.append("Voiture")
	tableau_nom_entite.append("Vendeur")
	tableau_nom_association.append("Achete")
	a=[]

	a.append("Id_client")
	a.append("Nom")
	a.append("prenom")
	a.append("adresse")
	tableau_attributs_entite.append(a)
	
	b=[]
	b.append("Numero_matricule")
	b.append("Marque")
	b.append("Prix")
	b.append("Couleur")
	tableau_attributs_entite.append(b)

	c=[]
	c.append("Id_vendeur")
	c.append("Nom")
	c.append("Prenom")
	c.append("adresse")
	tableau_attributs_entite.append(c)
	d=[]
	d.append("Date")
	tableau_attributs_association.append(d)