#!/usr/bin/python
# -*- coding: latin-1 -*-
from FuncionesNucleo import FuncionesNucleo
from ModeloSIR import ModeloSIR
import matplotlib.pyplot as plt
from igraph import *


class Simulacion2(object):

    def main(self):
        """ En esta segunda simulación vamos a comprobar como afecta
         en una epidemia si el virus empieza en un hub o no. """

        tam = 100000
        resultados = []

        print "Simulacion 1"
        resultados.append(FuncionesNucleo().simulacionHub(ModeloSIR,
                                                          "Scale_Free",
                                                          tam_grafo=tam,
                                                          susceptibles=tam,
                                                          time=300, beta=0.025,
                                                          gamma=0.01))
        print "Simulacion 2"
        resultados.append(
            FuncionesNucleo().simulacionAntiHub(ModeloSIR, "Scale_Free",
                                                tam_grafo=tam,
                                                susceptibles=tam,
                                                time=300, beta=0.025,
                                                gamma=0.01))

        tiempo = range(300)
        averaged = [mean(items) for items in izip(*resultados[0])]
        averaged2 = [mean(items) for items in izip(*resultados[1])]

        plt.plot(tiempo, averaged, 'r',
                 label='Infeccion iniciada en un hub')
        plt.plot(tiempo, averaged2, 'b',
                 label='Infeccion no iniciada en un hub')
        plt.legend(title="Hubs vs nodos normales")
        plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
        plt.savefig('Figuras/simulacion2.png')


ejec = Simulacion2()
ejec.main()
