import csv  # on peut aussi utiliser from csv import *
import random
from typing import List

f = open("scientifiques.csv", "r")

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


def choix_mot(mots: List[str]) -> str:
    """

    :param mots:
    :return:
    """
    return random.choice(mots)


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


def play(mot: str) -> None:
    """
    Lance la partie.
    Actions à effectuer:
        - Afficher l'état d'avancement du mot à deviner
        - Afficher le nombre de coups restants : info
        - Demander à l'utilisateur de rentrer une lettre : input_letter
        - Dire si réussi ou raté : info
        - Afficher si gagné ou perdu : check
        - Faire une boucle du programme tant que ce n'est pas perdu ou gagné.
    :return:
    :param mot: mot à découvrir
    :return:
    """
    pass


def display(mot):
    """
    Affiche les "_" pour représenter les lettres du mot et le nombre d'essais restants.
    :return:
    """
    mot_deviner = ["_" * len(mot)]
    # mot_affiche = mot_deviner[0]
    print(mot_deviner)


def info(mot: str) -> None:
    """

    :param mot:
    :return:
    """
    mot_remplace = display(mot)
    lettres_trouvees = []  # contient les lettres trouvées
    lettres_jouees = []  # contient les lettres jouées
    lettre = input_letter()

    if lettre in mot:
        lettres_trouvees.append(lettre)
        lettres_jouees.append(lettre)
        for lettre in range(mot):
            mot_remplace.append(lettre)
        print("Réussi !")
    else:
        lettres_jouees.append(lettre)
        print("Raté !")


def check():
    """
    Afficher si l'utilisateur a gagné ou perdu
    :return:
    """

    pass


def main():
    lettres_jouees = []
    mot_remplace = []
    noms = listenoms(table)
    mot_majuscule = metenmajuscule(noms)
    mot_random = choix_mot(mot_majuscule)
    print(mot_random)

    max_lettres = 8

    while len(lettres_jouees) < max_lettres or mot_remplace != mot_random:
        print(display(mot_random))
        nbr_essaies = 8
        print('il reste', nbr_essaies, "essaies")
        lettre_choisi = input_letter()
        lettres_jouees.append(lettre_choisi)
        print(lettres_jouees)
        nbr_essaies -= 1
        pass


if __name__ == '__main__':
    main()












"""
class Pendu:

    def __init__(self):
        pass

    def play(self, mot: str) -> None:

        Lance la partie.
        Actions à effectuer:
            - Afficher les "_" : display
            - Demander à l'utilisateur de rentrer une lettre : input_letter
            - Dire si réussi ou raté : info
            - Afficher le nombre de coups restants : info
            - Afficher si gagné ou perdu : check
        :return:
        :param mot: mot à découvrir
        :return:

        pass

    def display(self):

        Affiche les "_" pour représenter les lettres du mot et le nombre d'essais restants.
        :return:

        for i in range(len(motRandom)):
            mot_cache = "_" + i
        print(mot_cache)

    def info(self):

        Dis si coup raté ou réussi
        et afficher le nombre de coups restants
        :return:

        pass

    def check(self):

        Afficher si l'utilisateur a gagné ou perdu
        :return:

        pass



Actions à effectuer:
    - Afficher les "_"
    - Demander à l'utilisateur de rentrer une lettre
    - Dire si réussi ou raté
    - Afficher le nombre de coups restants
    - Afficher si gagné ou perdu



def main():
    pendu = Pendu()
    pendu.display()


main() """
