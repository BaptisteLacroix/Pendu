from penduClass import Pendu
from tkinter import *


# TODO: voir heritage Tk

class PenduGUI(Pendu):

    def __init__(self):
        super().__init__()
        self.window = Tk()
        self.configure_display()

    def configure_display(self):
        """
        Configure la fenêtre.
        -nomme la fenêtre
        -définit les dimensions
        :return:
        """
        self.window.title("Pendu")
        self.window.geometry("1000x700")

    def affiche_mot(self, liste):
        pass

    def play(self):
        self.window.mainloop()


def main():
    pendu = PenduGUI()
    pendu.play()


main()
