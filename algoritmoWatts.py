# #!/usr/bin/python
# # -*- coding: latin-1 -*-
from igraph import *
import random

## Creamos grafo de anillo base.
g1 = Graph.Ring(50)

## Tenemos 20 nodos, ahora pongamosle nombres para trabajar
## con ellos
i = 1
for v in VertexSeq(g1):
    v['name'] = "%d" % i
    i += 1

## Ahora añadimos una arista que enlace cada vertice
## con el vecino de su vecino en el sentido horario
i = 1
while i < 49:
    g1.add_edge("%d" % i,"%d" % (i + 2))
    i += 1
## añadimos los dos ultimos ejes
g1.add_edge('49', '1')
g1.add_edge('50', '2')

layout = g1.layout_circle
plot(g1, "imagen1.png")
#plot.show()

## Aplicamos el proceso de rewire con probabilidad p
for v in VertexSeq(g1):
    ## Tenemos una probabilidad de 0.5 de recablear
    if random.random() < 0.5:
        ## Esta parte se encarga de escoger un eje
        ## aleatorio del vertice
        ## random.choice(g1.es.select(v.index))

        g1.delete_edges(random.choice(g1.es.select(v.index)).index)
        ## Escogemos el vertice al que enlazar
        aleatorio = int(round(random.uniform(0, 19), 0))
        while aleatorio == v.index:
            aleatorio = int(round(random.uniform(0, 20), 0))
        g1.add_edge(v.index, aleatorio)

plot(g1, "imagen2.png")

## Aplicamos otra ronda
for v in VertexSeq(g1):
    ## Tenemos una probabilidad de 0.5 de recablear
    if random.random() < 0.5:
        ## Esta parte se encarga de escoger un eje
        ## aleatorio del vertice
        ## random.choice(g1.es.select(v.index))

        g1.delete_edges(random.choice(g1.es.select(v.index)).index)
        ## Escogemos el vertice al que enlazar
        aleatorio = int(round(random.uniform(0, 19), 0))
        while aleatorio == v.index:
            aleatorio = int(round(random.uniform(0, 20), 0))
        g1.add_edge(v.index, aleatorio)

plot(g1, "imagen3.png")