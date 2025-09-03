"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
DATA = './files/input/data.csv'

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    total = 0

    with open(DATA, "r", newline="") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            total += int(row[1])

    return total
