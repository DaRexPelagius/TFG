#!/usr/bin/python
# -*- coding: latin-1 -*-
from FuncionesNucleo import FuncionesNucleo
from ModeloSIR import ModeloSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion7(object):

    def main(self):
        """En esta simulacion veremos la influencia de gamma  en la
        propagación del malware. Fijaremos beta y realizaremos la
        simulacion para seis gammas distintas. """

        tam = 100000
        tiempo = 100
        beta = 0.025
        gamma = [0, 0.005, 0.01, 0.015, 0.02, 0.025]
        resultados = []

        i = 0
        for g in gamma:
            print "Simulacion %.3f" % g
            aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR, "Scale_Free",
                                               tam_grafo=tam, time=tiempo,
                                               beta=beta, gamma=g)

                ## CdE
            media = [mean(items) for items in izip(*aux2)]

            i = 0
            # while abs(mean(media)) - 0.05 < 0:
            #     print "Ronda %d" % i
            #     aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR, "Scale_Free",
            #                                        tam_grafo=tam, time=tiempo,
            #                                        beta=beta, gamma=g)
            #     media = [mean(items) for items in izip(*aux2)]
            #     i += 1
            # # Anyadimos el resultado
            resultados.append(aux)

        tiempo = range(tiempo)
        averaged = [mean(items) for items in izip(*resultados[0])]
        averaged2 = [mean(items) for items in izip(*resultados[1])]
        averaged3 = [mean(items) for items in izip(*resultados[2])]
        averaged4 = [mean(items) for items in izip(*resultados[3])]
        averaged5 = [mean(items) for items in izip(*resultados[4])]
        averaged6 = [mean(items) for items in izip(*resultados[5])]

        plt.plot(tiempo, averaged, 'r', label='Gamma = 0')
        plt.plot(tiempo, averaged2, 'b', label='Gamma = 0.005')
        plt.plot(tiempo, averaged3, 'g', label='Gamma = 0.01')
        plt.plot(tiempo, averaged4, 'fuchsia', label='Gamma = 0.015')
        plt.plot(tiempo, averaged5, 'black', label='Gamma = 0.02')
        plt.plot(tiempo, averaged6, 'greenyellow', label='Gamma = 0.025')
        plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
        plt.legend()
        plt.show()
        #plt.savefig('Figuras/simulacion1.png')


ejec = Simulacion7()
ejec.main()
