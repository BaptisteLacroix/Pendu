import csv  # on peut aussi utiliser from csv import *
import random
from typing import List

f = open("liste.de.mots.francais.frgut.csv", "r")

table = list(csv.reader(f, delimiter=';'))  # par défaut le délimiteur est la virgule


# print("table : ", table)


def listenoms(table):
    """

    :param table:
    :return:
    """
    return [value[0] for value in table[1:]]


def remove_accents(mot: str) -> str:
    """

    :param mot:
    :return:
    """
    phrase2 = ''
    d = {"à": "a", "À": "A", "â": "a", "Â": "A", "ã": "a", "Ã": "A", "A®": "i", "Ã©": "ai", "ç": "c", "Ç": "C",
         "é": "e", "É": "E", "è": "e", "È": "E", "ê": "e", "¨": "i",
         "Ê": "E", "ë": "e", "Ë": "E", "î": "i", "Î": "I", "ï": "i", "Ï": "I", "ô": "o", "Ô": "O", "ù": "u", "Ù": "U",
         "û": "u", "Û": "U", "ü": "u", "Ü": "U", "¢": "c", "$": "c", "§": "c"}
    for lettre in mot:
        if lettre in d:
            phrase2 += d[lettre]
        else:
            phrase2 += lettre
    return phrase2


def metenmajuscule(mots):
    """

    :param mots:
    :return:
    """
    return [mot.upper() for mot in mots]


def choix_mot(mots: List[str]) -> str:
    """

    :param mots:
    :return:
    """
    return random.choice(mots)


def affiche_mot(liste):
    """

    :param liste:
    :return:
    """
    mot = ''
    for i in liste:  # on parcourt la liste
        mot += i  # on ajoute chaque caractère au mot
    print(mot)


def main(mot):
    liste_lettre = list(mot)

    lettres_jouees = []  # contient les lettres jouées
    nbr_lettres_trouvees = 0  # contient le nombre de lettres trouvées

    liste_cherchee = ['_' for i in range(len(liste_lettre))]

    # print(mot_random)
    coups_perdus = 0
    coups_perdus_max = 8
    nbr_essaies = 8
    affiche_mot(liste_cherchee)
    lettre1 = str("-")
    lettre2 = "©"

    while nbr_lettres_trouvees < len(mot) or coups_perdus >= coups_perdus_max:
        if lettre1 in mot_random or lettre2 in mot_random:
            print("Attention il y a soit un '-' soit un '©' ;-)")

        print('il reste', nbr_essaies, "essaies")

        lettre = str(input("Entrer une lettre en MAJUSCULE : "))
        while lettre != lettre.upper() or len(lettre) != 1 or lettre in lettres_jouees:
            lettre = str(input("Entrer une lettre en MAJUSCULE : "))

        if lettre in mot_random:
            lettres_jouees.append(lettre)
            for i in range(len(liste_lettre)):
                if lettre == liste_lettre[i]:
                    liste_cherchee[i] = lettre  # remplace les '_' par les lettres trouvées
                    nbr_lettres_trouvees += 1
            print("Réussi !")
        else:
            lettres_jouees.append(lettre)
            print("Raté !")
            nbr_essaies -= 1
            coups_perdus += 1

        affiche_mot(liste_cherchee)

    if coups_perdus >= coups_perdus_max:
        print("Perdu !")
    else:
        print("Gagné !")


if __name__ == '__main__':
    noms = listenoms(table)
    mot_random = choix_mot(noms)
    mot_minuscule_sans_accents = remove_accents(mot_random)
    mot_majuscule = metenmajuscule(mot_minuscule_sans_accents)
    mot_random = "".join(mot_majuscule)

    main(mot_random)

f.close()  # il faut penser à fermer le fichier qui a été ouvert
