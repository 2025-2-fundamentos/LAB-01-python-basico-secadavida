"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from collections import defaultdict
import csv
DATA = './files/input/data.csv'


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """


    letters = defaultdict(int)

    with open(DATA, 'r', newline="") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            letter = row[0]
            letters[letter] += 1

    sorted_alphabetically = sorted(letters.items())

    return sorted_alphabetically
