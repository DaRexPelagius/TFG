#!/usr/bin/python
# -*- coding: latin-1 -*-
import math
from FuncionesNucleo import FuncionesNucleo
from ModeloSIR import ModeloSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion4(object):

    def main(self):
        """ En esta simulacion procederemos a ver cuanto mejora
        un gusano si le metemos intelegencia. En nuestra simulación,
        usaremos un nodo de tam 10^5, en el que supondremos como tres
        cuartas partes de la poblacion es susceptible, y empieza con tres
        infectados. Estos tres infectados tendrán probabilidad 1 de infectar
        a nodos con mayor grado que la media en los 5 primeros contactos, y 0
        en caso contrario. Después la epidemia se ejecuta con los valores de
        transición de las simulaciones anteriores. Por otra parte,
        se simulará la misma prueba sin contar esta inteligencia."""


        tam = 10 ** 5
        resultados = []

        """ Simulacion 1 """
        resultados.append(FuncionesNucleo().simulacionInteligente2(ModeloSIR,
                        "Scale_Free", tam_grafo=tam, susceptibles=tam,
                        time=300, beta=0.025, gamma=0.001))

        tiempo = range(300)
        averaged = [mean(items) for items in izip(*resultados[0])]
        plt.plot(tiempo, averaged, 'r', label='Infeccion inteligente')



        """ Simulacion 2 """
        resultados.append(FuncionesNucleo().simulacion(ModeloSIR, "Scale_Free",
                          tam_grafo=tam, susceptibles=tam, time=300,
                          beta=0.025, gamma=0.001))

        tiempo = range(300)
        averaged2 = [mean(items) for items in izip(*resultados[1])]
        plt.plot(tiempo, averaged2, 'b', label='Infeccion aleatoria')

        """ Generar grafica """
        plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
        plt.legend()
        plt.savefig('Figuras/simulacion4.png')


ejec = Simulacion4()
ejec.main()