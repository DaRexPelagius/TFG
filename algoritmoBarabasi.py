# #!/usr/bin/python
# # -*- coding: latin-1 -*-
from igraph import *
import random
import numpy as np

def preferalAttachment(grafo, nodo):
    flag_menor = 0
    flag_media = 0
    flag_mayor = 0
    fin = 0

    ## Empezamos calculando los cuatro percentiles
    grados = sorted(grafo.degree())
    mayor = round(np.percentile(grados, 75))
    media = round(np.percentile(grados, 50))
    menor = round(np.percentile(grados, 25))



    aleat = random.choice(grafo.vs)
    while fin != 1:
        ## Evitamos los bucles
        if nodo == aleat:
            aleat = random.choice(grafo.vs)
            break

        ejes1 = grafo.es.select(_source=aleat.index)
        ejes2 = grafo.es.select(_source=aleat.index)
        flag = 0
        for e in ejes1:
            flag = e in grafo.es.select(_source=nodo.index)
            if flag:
                break

        if flag:
            break

        if aleat.degree() > mayor:
            grafo.add_edge(nodo, aleat)
            fin = 1
        elif aleat.degree() > media:
            if flag_mayor >= 1:
                grafo.add_edge(nodo, aleat)
                fin = 1
            else:
                flag_mayor += 1
        elif aleat.degree() > menor:
            if flag_media >= 2:
                grafo.add_edge(nodo, aleat)
                fin = 1
            else:
                flag_media += 1
        else:
            if flag_menor >= 3:
                grafo.add_edge(nodo, aleat)
                fin = 1
            else:
                flag_menor += 1

def ajustarTamanyo(grafo):
    grados = sorted(grafo.degree())
    mayor = round(np.percentile(grados, 75))
    media = round(np.percentile(grados, 50))
    menor = round(np.percentile(grados, 25))

    for v in VertexSeq(g1):
        if v.degree() > mayor:
            v['size'] = 60
        elif v.degree() > media:
            v['size'] = 40
        elif v.degree() > menor:
            v['size'] = 25
        else:
            v['size'] = 15

## Vamos a ejemplificar como nace una
## red scale free. Para ello supondremos
## que los nodos con grado superior al grado
## medio tienen una probabilidad d
g1 = Graph()
i = 0
j = 0
nombres_fichero = ["imagen1sf.png", "imagen2sf.png", "imagen3sf.png",
                   "imagen4sf.png", "imagen5sf.png", "imagen6sf.png"]

print nombres_fichero

g1.add_vertex()
g1.add_vertex()
g1.add_edge(g1.vs[0], g1.vs[1])

while i < 30:
    g1.add_vertex()
    preferalAttachment(g1, g1.vs[i+2])
    preferalAttachment(g1, g1.vs[i+2])
    if (i % 5) == 0:
        if i != 0:
            ajustarTamanyo(g1)
        plot(g1, nombres_fichero[j], vertex_label = g1.degree())
        j += 1
    i += 1

plot(g1, vertex_label = g1.degree() )