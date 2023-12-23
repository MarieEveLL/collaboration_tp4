import pytest
from contenu import *


def test_initialization():
    assert add("") == "0"
    assert add("3") == "3"
    assert add("17,3") == "20"


def test_NbArbitraire():
    assert add("17,3,5,2,3") == "30"


def test_separateur():
    assert add("17\n3") == "20"


def test_fichier():
    assert NbLignes("fichier.txt") == 5


def test_joueur_X():
    jeu = TicTacToe()
    jeu.jouer(0, 0, "X")
    assert jeu.plateau[0][0] == "X"


def test_joueur_0():
    jeu = TicTacToe()
    jeu.jouer(1, 1, "O")
    assert jeu.plateau[1][1] == "O"


def test_partie_terminee():
    jeu = TicTacToe()
    jeu.jouer(0, 0, "X")
    jeu.jouer(0, 1, "X")
    jeu.jouer(0, 2, "X")
    assert jeu.est_terminee() == True


def test_partie_non_terminee():
    jeu = TicTacToe()
    jeu.jouer(0, 0, "X")
    jeu.jouer(0, 1, "X")
    jeu.jouer(0, 2, "Y")
    assert jeu.est_terminee() == False


def test_gagnant():
    jeu = TicTacToe()
    jeu.jouer(0, 0, "X")
    jeu.jouer(0, 1, "X")
    jeu.jouer(0, 2, "X")
    assert jeu.gagnant() == "X"
    assert jeu.gagnant() != "0"
