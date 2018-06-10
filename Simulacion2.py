#!/usr/bin/python
# -*- coding: latin-1 -*-
from FuncionesNucleo import *
from ModeloSIS import ModeloSIS
import matplotlib.pyplot as plt

""" En esta segunda simulación vamos a comprobar como afecta
 en una epidemia si el virus empieza en un hub o no. """

tam = 100000
resultados = []

resultados.append(simulacion(ModeloSIS, "Scale_Free", tam_grafo=tam, susceptibles=tam, hub=2, time=100, beta=0.25, gamma=0.1))
resultados.append(simulacion(ModeloSIS, "Scale_Free", tam_grafo=tam, susceptibles=tam, hub=1, time=100, beta=0.25, gamma=0.1))

tiempo = range(100)
averaged = [mean(items) for items in izip(*resultados[0])]
averaged2 = [mean(items) for items in izip(*resultados[1])]

plt.plot(tiempo, averaged, 'r', label='Infeccion iniciada en un hub')
plt.plot(tiempo, averaged2, 'b', label='Infeccion no iniciada en un hub')
plt.legend(title="Hubs vs nodos normales")
plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
plt.show()