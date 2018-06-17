#!/usr/bin/python
# -*- coding: latin-1 -*-
import math
from FuncionesNucleo import FuncionesNucleo
from ModeloXSIR import ModeloXSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion5(object):

    def main(self):
        """ En esta simulación comprobaremos """
        tam = 10 ** 5
        resultados = []

        """ Simulacion 1 """
        resultados.append(FuncionesNucleo().simulacionGrupoInicial(ModeloXSIR,
                        "Scale_Free", tam_grafo=tam, susceptibles=tam*0.8,
                        n_infectados=3, time=100, beta=0.025, gamma=0.01,
                        runs=10))


        """ Generar grafica """
        plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
        plt.legend()
        plt.savefig('Figuras/simulacion6.png')


ejec = Simulacion5()
ejec.main()