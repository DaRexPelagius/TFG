#!/usr/bin/python
# -*- coding: latin-1 -*-
from FuncionesNucleo import FuncionesNucleo
from ModeloSIR import ModeloSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion1(object):

    def main(self):
        """En esta primera simulacion vamos a ver como influye el tamanyo
        de la poblacion en el porcentaje de poblacion en cada compartimento.
        Para ello realizaremos la simulacion sobre un grafo en un periodo de
        100 unidades de tiempo para tamanyos desde 100 a 1000000."""

        tam = [100, 1000, 5000, 10000, 25000, 50000, 100000, 1000000]
        tiempo = 100
        beta = 0.025
        gamma = 0.01
        resultados = []

        for s in tam:
            print "Simulacion 1 Tamanyo: %d" % s
            if s != 1000000:
                aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR,
                                                         "Scale_Free",
                                                         tam_grafo=s,
                                                         time=tiempo,
                                                         beta=beta, gamma=gamma)

                ## CdE
                media = [mean(items) for items in izip(*aux2)]
                while abs(mean(media)) - 0.05 < 0:
                    aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR,
                                                             "Scale_Free",
                                                             tam_grafo=s,
                                                             time=tiempo,
                                                             beta=beta,
                                                             gamma=gamma)
                    media = [mean(items) for items in izip(*aux2)]
                # Anyadimos el resultado
                resultados.append(aux)

                # La simulacion con un millon de nodos solo la haremos una vez
                # por limitaciones del HW.
            else:
                aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR,
                                                         "Scale_Free",
                                                         tam_grafo=s, runs=1,
                                                         time=tiempo, beta=beta,
                                                         gamma=gamma)

                ## CdE
                media = [mean(items) for items in izip(*aux2)]
                while abs(mean(media)) - 0.05 < 0:
                    aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR,
                                                             "Scale_Free",
                                                             tam_grafo=s,
                                                             time=tiempo,
                                                             beta=beta,
                                                             gamma=gamma)
                    media = [mean(items) for items in izip(*aux2)]
                # Anyadimos el resultado
                resultados.append(aux)

        tiempo = range(tiempo)
        averaged = [mean(items) for items in izip(*resultados[0])]
        averaged2 = [mean(items) for items in izip(*resultados[1])]
        averaged3 = [mean(items) for items in izip(*resultados[2])]
        averaged4 = [mean(items) for items in izip(*resultados[3])]
        averaged5 = [mean(items) for items in izip(*resultados[4])]
        averaged6 = [mean(items) for items in izip(*resultados[5])]
        averaged7 = [mean(items) for items in izip(*resultados[6])]
        averaged8 = [mean(items) for items in izip(*resultados[7])]

        plt.plot(tiempo, averaged, 'r', label='n = 100')
        plt.plot(tiempo, averaged2, 'b', label='n = 1000')
        plt.plot(tiempo, averaged3, 'g', label='n = 5000')
        plt.plot(tiempo, averaged4, 'fuchsia', label='n = 10000')
        plt.plot(tiempo, averaged5, 'black', label='n = 25000')
        plt.plot(tiempo, averaged6, 'greenyellow', label='n = 50000')
        plt.plot(tiempo, averaged7, 'cyan', label='n = 1000000')
        plt.plot(tiempo, averaged8, 'brown', label='n = 10000000')
        plt.legend(title="Numero de nodos del grafo")
        plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
        plt.show()
        #plt.savefig('Figuras/simulacion1.png')


ejec = Simulacion1()
ejec.main()
