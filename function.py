#!/usr/bin/python3
# encoding: utf-8
from random import randint
import random
import csv
import math

class FuncionesGeneticas:
    def __init__(self, path):
        # El path para leer el archivo csv
        self.path = path

    # -------------------------
    # Retorna el valor fitness
    # Duda = al ser un w negativo, la nota es negativa
    def evaluar(self, solucion):
        value = 0.0

        with open(self.path, newline='') as csvfile:
            next(csvfile)  # Skip header
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')

            print(solucion)
            for row in spamreader:
                P1 = float(row[0])
                P2 = float(row[1])
                P3 = float(row[2])
                W1 = float(solucion[0])
                W2 = float(solucion[1])
                W3 = float(solucion[2])
                NR = float(row[3])

                print(P1)

                NC = W1*P1 + W2*P2 + W3*P3
                #(𝑁𝑅𝑖 − 𝑁𝐶𝑖)^2
                value += math.pow((NR - NC), 2)
        return round(value/4, 2)
