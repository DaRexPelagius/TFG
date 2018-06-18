#!/usr/bin/python
# -*- coding: latin-1 -*-
import math
from FuncionesNucleo import FuncionesNucleo
from ModeloSIR import ModeloSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion6(object):

    def main(self):
        """ En esta simulación comprobaremos como afecta que los primeros
         infectados esten juntos o no. """
        tam = 10 ** 5
        tiempo = 100
        beta = 0.025
        gamma = 0.01
        runs = 10
        resultados = []

        print "Simulacion 1"
        aux, aux2 = FuncionesNucleo().simulacionGrupoInicial(ModeloSIR,
                                                             "Scale_Free",
                                                             tam_grafo=tam,
                                                             n_infectados=3,
                                                             time=tiempo,
                                                             beta=beta,
                                                             gamma=gamma,
                                                             runs=runs)
        ## CdE
        # media = [mean(items) for items in izip(*aux2)]
        # while abs(mean(media)) - 0.05 < 0:
        #     aux, aux2 = FuncionesNucleo().simulacionGrupoInicial(ModeloXSIR,
        #                 "Scale_Free", tam_grafo=tam, susceptibles=tam*0.8,
        #                 n_infectados=3, time=tiempo, beta=beta, gamma=gamma,
        #                 runs=runs)
        #     media = [mean(items) for items in izip(*aux2)]

        resultados.append(aux)

        print "Simulacion 2"
        aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR,
                                                 "Scale_Free", tam_grafo=tam,
                                                 n_infectados=3, time=tiempo,
                                                 beta=beta, gamma=gamma,
                                                 runs=runs)
        ## CdE
        # media = [mean(items) for items in izip(*aux2)]
        # while abs(mean(media)) - 0.05 < 0:
        #     aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR,
        #                 "Scale_Free", tam_grafo=tam, susceptibles=tam*0.8,
        #                 n_infectados=3, time=tiempo, beta=beta, gamma=gamma,
        #                 runs=runs)
        #     media = [mean(items) for items in izip(*aux2)]

        resultados.append(aux)

        tiempo = range(tiempo)
        averaged = [mean(items) for items in izip(*resultados[0])]
        averaged2 = [mean(items) for items in izip(*resultados[1])]

        plt.plot(tiempo, averaged, 'r',
                 label='Grupo inicial junto')
        plt.plot(tiempo, averaged2, 'b',
                 label='Grupo inicial disperso')
        plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
        plt.legend()
        # Plot
        plt.show()
        # plt.savefig('Figuras/simulacion2.png')


ejec = Simulacion6()
ejec.main()