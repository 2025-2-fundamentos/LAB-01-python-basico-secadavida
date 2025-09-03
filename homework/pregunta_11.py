"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
from collections import defaultdict

DATA = './files/input/data.csv'


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sums = defaultdict(int)

    with open(DATA, "r", newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            value = int(row[1])
            letters = row[3].split(",")

            for letter in letters:
                if letter:
                    sums[letter] += value

    alphabetically_sorted = dict(sorted(sums.items()))

    return alphabetically_sorted
