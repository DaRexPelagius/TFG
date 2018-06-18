#!/usr/bin/python
# -*- coding: latin-1 -*-
from FuncionesNucleo import *
from ModeloXSIR import ModeloXSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion3(object):

    def main(self):
        """ En esta simulacion procederemos a ver cuanto mejora
        un gusano si le metemos intelegencia. En nuestra simulación,
        usaremos un nodo de tam 10^5, en el que supondremos como tres
        cuartas partes de la poblacion es susceptible, y empieza con tres
        infectados. Estos tres infectados tendrán probabilidad 1 de infectar
        a nodos con un grado alto (perc. 90) en los 5 primeros contactos, y
        0 en caso contrario. Después la epidemia se ejecuta con los valores
        de transición de las simulaciones anteriores. Por otra parte, se
        simulará la misma prueba sin contar esta inteligencia."""

        tam = 10 ** 5
        tiempo = 100
        beta = 0.025
        gamma = 0.01
        resultados = []

        """ Simulacion 1 """
        print "Simulacion 1"
        aux, aux2 = FuncionesNucleo().simulacionInteligente(ModeloXSIR,
                                                            "Scale_Free",
                                                            tam_grafo=tam,
                                                            susceptibles=tam,
                                                            n_infectados=5,
                                                            time=tiempo,
                                                            beta=beta,
                                                            gamma=gamma)
        ## CdE
        media = [mean(items) for items in izip(*aux2)]
        i = 2
        while abs(mean(media)) - 0.005 < 0:
            print "Intento %d" % i
            print "Media: %.3f" % abs(mean(media))
            i += 1
            aux, aux2 = FuncionesNucleo().simulacionInteligente(ModeloXSIR,
                                                                "Scale_Free",
                                                                tam_grafo=tam,
                                                               susceptibles=tam,
                                                                n_infectados=5,
                                                                time=tiempo,
                                                                beta=beta,
                                                                gamma=gamma)
            media = [mean(items) for items in izip(*aux2)]

        resultados.append(aux)

        t = range(tiempo)
        averaged = [mean(items) for items in izip(*resultados[0])]
        plt.plot(t, averaged, 'r', label='Infeccion inteligente')

        """ Simulacion 2 """
        print "Simulacion 2"
        aux, aux2 = FuncionesNucleo().simulacion(ModeloXSIR,
                                                 "Scale_Free", tam_grafo=tam,
                                                 susceptibles=tam,
                                                 n_infectados=5,
                                                 time=tiempo, beta=beta,
                                                 gamma=gamma)
        ## CdE
        media = [mean(items) for items in izip(*aux2)]
        i = 2
        while abs(mean(media)) - 0.005 < 0:
            print "Intento %d" % i
            print "Media: %.3f" % abs(mean(media))
            i += 1
            aux, aux2 = FuncionesNucleo().simulacion(ModeloXSIR,
                                                     "Scale_Free",
                                                     tam_grafo=tam,
                                                     susceptibles=tam,
                                                     n_infectados=5,
                                                     time=tiempo, beta=beta,
                                                     gamma=gamma)
            media = [mean(items) for items in izip(*aux2)]

        resultados.append(aux)

        t = range(tiempo)
        averaged2 = [mean(items) for items in izip(*resultados[1])]
        plt.plot(t, averaged2, 'b', label='Infeccion aleatoria')

        """ Generar grafica """
        plt.title("Proporcion de infectados a lo largo de %du de tiempo."
                  % tiempo)
        plt.legend()
        plt.show()
        # plt.savefig('Figuras/simulacion3.png')


ejec = Simulacion3()
ejec.main()
