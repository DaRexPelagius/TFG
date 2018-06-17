#!/usr/bin/python
# -*- coding: latin-1 -*-
import math
from FuncionesNucleo import FuncionesNucleo
from ModeloXSIR import ModeloXSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion5(object):

    def main(self):
        """ En esta simulación colorearemos los compartimentos distintos
        para ver de una forma visual la propagación del malware, en un caso
        con parametros obtenidos del caso 'Wannacry'."""
        tam = 10 ** 2
        resultados = []

        """ Simulacion 1 """
        resultados.append(FuncionesNucleo().simulacionColores(ModeloXSIR,
                        "Scale_Free", tam_grafo=tam, susceptibles=tam*0.5,
                        n_infectados=3, time=14, beta=0.8, gamma=0.007,
                        runs=1))




ejec = Simulacion5()
ejec.main()