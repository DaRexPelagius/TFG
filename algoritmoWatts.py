# #!/usr/bin/python
# # -*- coding: latin-1 -*-
from igraph import *
import random
import numpy as np

def ajustarTamanyo(grafo):
    grados = sorted(grafo.degree())
    mayor = round(np.percentile(grados, 75))
    media = round(np.percentile(grados, 50))
    menor = round(np.percentile(grados, 25))

    for v in VertexSeq(g1):
        if v.degree() > mayor:
            v['color'] = 'cyan'
            v['size'] = 60
        elif v.degree() > media:
            v['color'] = 'yellow'
            v['size'] = 40
        elif v.degree() > menor:
            v['color'] = 'green'
            v['size'] = 25
        else:
            v['color'] = 'red'
            v['size'] = 15


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
plot(g1, "imagen1sw.png", vertex_label = g1.degree())
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

ajustarTamanyo(g1)
plot(g1, "imagen2sw.png", vertex_label = g1.degree())

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

ajustarTamanyo(g1)
plot(g1, "imagen3sw.png", vertex_label = g1.degree())


plot(g1, vertex_label = g1.degree() )