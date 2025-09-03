"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

DATA = './files/input/data.csv'


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    values = []

    with open(DATA, "r", newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            id = row[0]
            len_letters = len(row[3].split(","))
            len_elements = len(row[4].split(","))

            values.append(
                (id, len_letters, len_elements)
            )

    return values
