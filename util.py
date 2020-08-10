import csv  # on peut aussi utiliser from csv import *
import random

f = open("C:/Users/k/Desktop/Langage informatique/programmation/NSI/ExercicesCours/Confinement/TraitementDeDonnees"
         "/Traitementdedonnes2/scientifiques.csv", "r")

table = list(csv.reader(f, delimiter=';'))  # par défaut le délimiteur est la virgule

f.close()  # il faut penser à fermer le fichier qui a été ouvert


# print("table : ", table)


def listenoms(table):
    """

    :param table:
    :return:
    """
    # Values = table[1:]
    # Values2 = []

    """for i in range(len(Values)):
        Values2.append(Values[i][0])
    return Values2"""

    """for value in Values:
        Values2.append(value[0])
    return Values2"""

    return [value[0] for value in table[1:]]


def metenmajuscule(mots):
    """

    :param mots:
    :return:
    """

    """motsMajuscules = []
    for mot in mots:
        motsMajuscules.append(mot.upper())
    return motsMajuscules"""

    return [mot.upper() for mot in mots]


def choix_mot(motMajuscule):
    """

    :param mots:
    :return:
    """
    return random.choice(motMajuscule)


def affiche_mot(lettres):
    """

    :param lettres:
    :return:
    """
    print("".join(lettres))


def input_letter():
    """
    Demande à l'utilisateur de rentrer une lettre
    :return:
    """
    lettre = str(input("Entrer une lettre en MAJUSCULE : "))
    while lettre != lettre.upper() or len(lettre) != 1:
        lettre = str(input("Entrer une lettre en MAJUSCULE : "))
    else:
        return lettre



noms = listenoms(table)
motMajuscule = metenmajuscule(noms)
motRandom = choix_mot(motMajuscule)
print(motRandom)
lettre_choisi = input_letter()
