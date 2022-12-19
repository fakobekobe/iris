from django import template

register = template.Library()

# Fonction de parcourt de liste
@register.filter
def liste(variable, parametre):
    try:
        return variable[parametre]
    except:
        return ""


def separateur_milliers(nombre, separateur=' ', milliers=3):
    """
        Cette fonction permet de séparer les milliers par un caractère donné (separateur)
        Elle renvoie le (nombre) formaté.
        milliers représente le nombre de caractères des milliers
        Ex: nombre = 14000500
            séparateur = ' '
            retour = 14 000 500

    """

    # les variables
    tableau = []

    # On parse le nombre car le type int ne fonctionne pas avec la fonction  len
    # ensuite on enleve les espaces avant et arrière puis on retire les espaces internes
    nombre = ((str(nombre)).strip()).replace(' ', '')
    longueur = len(nombre)  # On récupère le nombre de caractères

    nb_espace = longueur // milliers  # On récupère le nombre de caractères à ajouter
    reste = longueur % milliers  # On récupère le nombre de caractères restant
    pas = 0

    if nb_espace > 1:  # On vérifie si nous avons un nombre de plus de 6 caractères

        # On transforme la chaine en tableau
        for i in range(longueur):
            tableau.append(nombre[i])

        for i in range(nb_espace):  # On parcours le nombre d'espace à inserer
            pas = reste + (milliers * i) + i

            # On insert un espace à la position du pas
            tableau.insert(pas, separateur)

        # On transforme le tableau en chaine et on le retourne
        return (''.join(tableau)).lstrip(separateur)

    else:  # On traite les nombre de moins de 6 caractères
        if nb_espace == 1 and reste:
            # On transforme la chaine en tableau
            for i in range(longueur):
                tableau.append(nombre[i])

            # On insert un espace à la position du reste
            tableau.insert(reste, separateur)

            # On transforme le tableau en chaine et on le retourne
            return ''.join(tableau)
        else:
            return nombre

@register.filter
def separateur_millier(nombre):
    return separateur_milliers(nombre)
