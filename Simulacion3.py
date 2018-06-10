#!/usr/bin/python
# -*- coding: latin-1 -*-
import math
from FuncionesNucleo import *
from ModeloSIS import ModeloSIS
import matplotlib.pyplot as plt

""" En esta simulacion procederemos a ver cuanto mejora
un gusano si le metemos intelegencia. En nuestra simulación,
usaremos un nodo de tam 10^5, en el que supondremos como tres
cuartas partes de la poblacion es susceptible, y empieza con tres infectados.
Estos tres infectados tendrán probabilidad 1 de infectar a nodos con mayor
grado que la media en los 5 primeros contactos, y 0 en caso contrario. Después
la epidemia se ejecuta con los valores de transición de las simulaciones
anteriores. Por otra parte, se simulará la misma prueba sin contar esta inteligencia."""


tam = 10 ** 5
resultados = []

""" Simulacion 1 """
resultados.append(simulacionInteligente(ModeloSIS, "Scale_Free", tam_grafo=tam, susceptibles=tam, hub=2, time=100, beta=0.025, gamma=0.01))

tiempo = range(100)
averaged = [mean(items) for items in izip(*resultados[0])]
plt.plot(tiempo, averaged, 'r', label='Infeccion inteligente')



""" Simulacion 2 """
resultados.append(simulacion(ModeloSIS, "Scale_Free", tam_grafo=tam, susceptibles=tam, hub=2, time=100, beta=0.025, gamma=0.01))

tiempo = range(100)
averaged2 = [mean(items) for items in izip(*resultados[1])]
plt.plot(tiempo, averaged2, 'b', label='Infeccion aleatoria')

""" Generar grafica """
plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
plt.legend()
plt.savefig('simulacion3.png')