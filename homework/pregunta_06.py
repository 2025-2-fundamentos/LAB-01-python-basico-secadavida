"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
from collections import defaultdict

DATA = './files/input/data.csv'


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    values = defaultdict(list)

    with open(DATA, "r", newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            ids = row[4]

            for id in ids.split(","):
                letters, number = id.split(":")
                values[letters].append(int(number))

    res = []
    for letters in sorted(values.keys()):
        max_val = max(values[letters])
        min_val = min(values[letters])
        res.append((letters, min_val, max_val))

    return res
