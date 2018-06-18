#!/usr/bin/python
# -*- coding: latin-1 -*-
from FuncionesNucleo import FuncionesNucleo
from ModeloSIR import ModeloSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion2(object):

    def main(self):
        """ En esta segunda simulación vamos a comprobar como afecta
         en una epidemia si el virus empieza en un hub o no. Para ello
         utilizaremos los mismos parámetros que en el apartado anterior
         a la hora de realizar la simulacion, salvo a la hora de escoger el
         primer nodo infectado."""

        tam = 100000
        tiempo = 100
        beta = 0.025
        gamma = 0.01
        resultados = []

        print "Simulacion 1"
        aux, aux2 = FuncionesNucleo().simulacionHub(ModeloSIR,
                                                    "Scale_Free",
                                                    tam_grafo=tam,
                                                    time=tiempo, beta=beta,
                                                    gamma=gamma)
        ## CdE
        media = [mean(items) for items in izip(*aux2)]
        while abs(mean(media)) - 0.05 < 0:
            aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR, "Scale_Free",
                                                     tam_grafo=tam, time=tiempo,
                                                     beta=beta, gamma=gamma)
            media = [mean(items) for items in izip(*aux2)]

        resultados.append(aux)

        print "Simulacion 2"
        aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR, "Scale_Free",
                                                 tam_grafo=tam,
                                                 time=tiempo, beta=beta,
                                                 gamma=gamma)
        ## CdE
        media = [mean(items) for items in izip(*aux2)]
        while abs(mean(media)) - 0.05 < 0:
            aux, aux2 = FuncionesNucleo().simulacion(ModeloSIR, "Scale_Free",
                                                     tam_grafo=tam, time=tiempo,
                                                     beta=beta, gamma=gamma)
            media = [mean(items) for items in izip(*aux2)]

        resultados.append(aux)

        tiempo = range(tiempo)
        averaged = [mean(items) for items in izip(*resultados[0])]
        averaged2 = [mean(items) for items in izip(*resultados[1])]

        plt.plot(tiempo, averaged, 'r',
                 label='Infeccion iniciada en un hub')
        plt.plot(tiempo, averaged2, 'b',
                 label='Infeccion iniciada de forma aleatoria')
        plt.legend(title="Hubs vs nodos normales")
        plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
        # Plot
        plt.show()
        #plt.savefig('Figuras/simulacion2.png')


ejec = Simulacion2()
ejec.main()
