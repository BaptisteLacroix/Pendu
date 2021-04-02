# By Baptiste Lacroix / GitHub : https://github.com/BaptisteLacroix

import csv  # on peut aussi utiliser from csv import *
import random
from typing import List

f = open("liste-demots.csv", "r")

table = list(csv.reader(f, delimiter=';'))  # par défaut le délimiteur est la virgule


# print("table : ", table)


def listenoms(tableau):
    """

    :param tableau:
    :return:
    """
    return [value[0] for value in tableau[1:]]


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


class Pendu:

    lettre1 = "-"
    lettre2 = "©"
    coups_perdus_max = 8

    def __init__(self):
        self.mot = ''
        self.liste_lettre = list(self.pick_random_word())
        self.lettres_jouees = []
        self.nbr_lettres_trouvees = 0  # contient le nombre de lettres trouvées
        self.coups_perdus = 0
        self.nbr_essaies = 8
        self.liste_cherchee = ['_' for i in range(len(self.liste_lettre))]

    @staticmethod
    def pick_random_word() -> str:
        """
        Renvoie un mot choisi aléatoirement
        :return: le mot choisi
        """
        noms = listenoms(table)
        # print(noms)
        mot_random = choix_mot(noms)
        mot_minuscule_sans_accents = remove_accents(mot_random)
        mot_majuscule = metenmajuscule(mot_minuscule_sans_accents)
        return "".join(mot_majuscule)

    def asking(self):
        self.lettre = str(input("Entrer une lettre en MAJUSCULE : "))
        while self.lettre != self.lettre.upper() or len(self.lettre) != 1 or self.lettre in self.lettres_jouees:
            self.lettre = str(input("Entrer une lettre en MAJUSCULE : "))

    def check(self):
        """
        Afficher si l'utilisateur a gagné ou perdu
        :return:
        """
        if self.lettre in self.liste_lettre:
            self.lettres_jouees.append(self.lettre)
            for i in range(len(self.liste_lettre)):
                if self.lettre == self.liste_lettre[i]:
                    self.liste_cherchee[i] = self.lettre  # remplace les '_' par les lettres trouvées
                    self.nbr_lettres_trouvees += 1
                    self.mot = "".join(self.liste_cherchee)
            print("Réussi !")
        else:
            self.lettres_jouees.append(self.lettre)
            print("Raté !")
            self.nbr_essaies -= 1
            self.coups_perdus += 1

    def info(self):
        """
        Informe si il y a un caractère spécial
        :return:
        """
        if Pendu.lettre1 in self.liste_lettre or Pendu.lettre2 in self.liste_lettre:
            print("Attention il y a soit un '-' soit un '©' ;-)")

    def affiche_mot(self):
        """

        :param liste:
        :return:
        """
        for i in self.liste_cherchee:  # on parcourt la liste
            self.mot += i  # on ajoute chaque caractère au mot
        print(self.mot)

    def play(self):
        """
        Lance la partie.
        Actions à effectuer:
            - Afficher les "_" : display
            - Demander à l'utilisateur de rentrer une lettre : input_letter
            - Dire si réussi ou raté : info
            - Afficher le nombre de coups restants : info
            - Afficher si gagné ou perdu : check
        :return:
        """
        mot = "".join(self.liste_lettre)
        print(mot)
        self.affiche_mot()
        while self.nbr_lettres_trouvees < len(mot) and self.coups_perdus < Pendu.coups_perdus_max:
            self.info()
            print('il reste', self.nbr_essaies, "essaies")
            self.asking()
            self.check()
            print(self.mot)

        if self.coups_perdus >= self.coups_perdus_max:
            print("Perdu ! Le mot était", mot)
        else:
            print("Gagné !")


def main():
    # lance le jeu
    pendu = Pendu()
    pendu.play()


if __name__ == '__main__':
    main()

f.close()  # il faut penser à fermer le fichier qui a été ouvert
