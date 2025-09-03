"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
from collections import defaultdict

DATA = './files/input/data.csv'


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    values = defaultdict(list)

    with open(DATA, "r", newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            letter = row[0]
            number = int(row[1])

            values[letter].append(number)

    res = []
    for letter in sorted(values.keys()):
        max_val = max(values[letter])
        min_val = min(values[letter])
        res.append((letter, max_val, min_val))

    return res
