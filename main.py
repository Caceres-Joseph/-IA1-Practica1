#!/usr/bin/python3
# encoding: utf-8
from function import *


# Una posible solucion
individuo1 =  [0.45, 0.2, 0.34]

# Instanciando las funciones
func = FuncionesGeneticas("/home/joseph/Documentos/IA/Practica1/MC2A.csv")
print(func.evaluar(individuo1))
