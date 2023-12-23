import pytest


def add(numbers_str):
    numbers = numbers_str.replace("\n", ",")
    numbers = numbers.split(",")

    if len(numbers) == 0 or (len(numbers) == 1 and not numbers[0]):
        return "0"

    else:
        total = sum(int(num) for num in numbers if num.isdigit())
        return str(total)


def NbLignes(fichier):
    try:
        with open(fichier, "r") as file:
            lignes = file.readlines()
        return len(lignes)
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{fichier}' n'existe pas.")


class TicTacToe:
    def __init__(self):
        self.plateau = [[" " for _ in range(3)] for _ in range(3)]

    def jouer(self, x, y, joueur):
        if self.plateau[x][y] == " ":
            self.plateau[x][y] = joueur

    def est_terminee(self):
        for i in range(3):
            if (
                self.plateau[i][0] == self.plateau[i][1] == self.plateau[i][2] != " "
            ):  
                return True
            if (
                self.plateau[0][i] == self.plateau[1][i] == self.plateau[2][i] != " "
            ):  
                return True
        if (
            self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] != " "
        ):  
            return True
        if (
            self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] != " "
        ):  
            return True
        return False

    def gagnant(self):
        for i in range(3):
            if self.plateau[i][0] == self.plateau[i][1] == self.plateau[i][2] != " ":
                return self.plateau[i][0]
            if self.plateau[0][i] == self.plateau[1][i] == self.plateau[2][i] != " ":
                return self.plateau[0][i]
        if self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] != " ":
            return self.plateau[0][0]
        if self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] != " ":
            return self.plateau[0][2]
        return None
