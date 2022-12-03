from localisation.models import *

# Liste des méthodes Globales du projet--------

def ajoute_zero_a_identifiant(departement, ville, identifiant, taille_fixe=7):
	"""
		Cette méthode permet l'ajout d'un certain nombre de 0 avant
		la variable [identification] selon taille_fixe afin d'avoir une chaine concatennée
		Ex: departement="001" - ville="002" - identification="5"
			la valeur de retour = 0010020000005
	"""
	texte = departement + ville
	fin = str(identifiant)
	taille = len(fin)
	dif = taille_fixe - taille
	suite = ""
	if dif > 0:
		for n in range(dif):
			suite += "0"
		texte += suite + fin
	else:
		texte += fin
	return texte
#--------------------------------------------------

