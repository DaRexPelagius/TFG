#!/usr/bin/python
# -*- coding: latin-1 -*-
from FuncionesAuxiliares import *
from SISModel import SISModel
import matplotlib.pyplot as plt

""" En esta primera simulación vamos a ver como influye el tamaño de la población
en el porcentaje de población en cada compartimento. Para ello realizaremos la 
simulación sobre un grafo en un periodo de 100 unidades de tiempo para tamaños desde
1000 a 1mmm. """

tam = [100, 1000, 5000, 10000, 25000, 50000, 100000]
#tam = [100, 1000, 10000]

resultados = []

for s in tam:
	print s
	resultados.append(simulacion(SISModel, "Scale_Free", tam_grafo=s, time=100, beta=0.25, gamma=0.1))
#simulacion(modelo, tipo_grafo, tam_grafo=10000, hub=0, infectados=1, runs=10, time=100, *args, **kwds)
#for r in resultados:
	#print r

tiempo = range(100)
averaged = [mean(items) for items in izip(*resultados[0])]
averaged2 = [mean(items) for items in izip(*resultados[1])]
averaged3 = [mean(items) for items in izip(*resultados[2])]
averaged4 = [mean(items) for items in izip(*resultados[3])]
averaged5 = [mean(items) for items in izip(*resultados[4])]
averaged6 = [mean(items) for items in izip(*resultados[5])]
averaged7 = [mean(items) for items in izip(*resultados[6])]

plt.plot(tiempo, averaged, 'r', label='n = 100')
plt.plot(tiempo, averaged2, 'b', label='n = 1000')
plt.plot(tiempo, averaged3, 'g', label='n = 5000')
plt.plot(tiempo, averaged4, 'fuchsia', label='n = 10000')
plt.plot(tiempo, averaged5, 'black', label='n = 25000')
plt.plot(tiempo, averaged6, 'greenyellow', label='n = 50000')
plt.plot(tiempo, averaged7, 'cyan', label='n = 1000000')
plt.legend(title="Numero de nodos del grafo")
plt.title("Proporcion de infectados a lo largo de 100u de tiempo.")
plt.show()



#plot_results(resultados, ['r-o','b-o', 'g-o'])
#pylab.show()
