"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
from collections import defaultdict

DATA = './files/input/data.csv'


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    values = defaultdict(int)

    with open(DATA, "r", newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            ids = row[4]

            for id in ids.split(","):
                letters = id.split(":")[0]
                values[letters] += 1

    res = {}
    for letters in sorted(values.keys()):
        res[letters] = values[letters]

    return res
