"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
from collections import defaultdict

DATA = './files/input/data.csv'


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    months = defaultdict(int)

    with open(DATA, 'r', newline="") as file:
        reader = csv.reader(file, delimiter="\t")

        for row in reader:
            date = row[2]
            month = date.split("-")[1]

            months[month] += 1

    sorted_numerically = sorted(months.items())

    return sorted_numerically
