# #!/usr/bin/python
# # -*- coding: latin-1 -*-
from igraph import *
import numpy as np

class algoritmoBarabasi(object):

    def main(self):
        ## Vamos a ejemplificar como nace una
        ## red scale free. Para ello supondremos
        ## que los nodos con grado superior al grado
        ## medio tienen una probabilidad d
        g1 = Graph()
        i = 0
        j = 0
        nombres_fichero = ["imagen1sf.png", "imagen2sf.png", "imagen3sf.png",
                           "imagen4sf.png", "imagen5sf.png", "imagen6sf.png"]


        g1.add_vertex()
        g1.add_vertex()
        g1.add_edge(g1.vs[0], g1.vs[1])
        print g1.vs[0].degree()
        print g1.vs[1].degree()

        while i < 30:
            g1.add_vertex()
            self.preferalAttachment(g1, g1.vs[i + 2])
            self.preferalAttachment(g1, g1.vs[i + 2])
            if (i % 5) == 0:
                if i != 0:
                    self.ajustarTamanyo(g1)
                plot(g1, nombres_fichero[j], vertex_label=g1.degree())
                j += 1
            i += 1

        plot(g1, vertex_label=g1.degree())

    def preferalAttachment(self, grafo, nodo):
        fin = 0

        ## Empezamos calculando los cuatro percentiles
        grados = grafo.degree()
        sum_grados = np.sum(grados)

        ## Preparamos la distribucion de probabilidad
        dist_prob = []
        for v in grafo.vs:
            dist_prob.append(v.degree()/float(sum_grados))


        ## Escogemos un nodo aleatorio distinto del nuevo
        aleat = np.random.choice(grafo.vs, p=dist_prob)
        while fin != 1:
            ## Evitamos los bucles
            if nodo == aleat:
                aleat = np.random.choice(grafo.vs)
                break

            ## Comprobamos que no hay ejes repetidos
            ejes1 = grafo.es.select(_source=aleat.index)
            ejes2 = grafo.es.select(_source=aleat.index)
            flag = 0
            for e in ejes1:
                flag = e in grafo.es.select(_source=nodo.index)
                if flag:
                    break
            if flag:
                continue
            else:
                fin = 1


        ## Añadimos el eje
        grafo.add_edge(nodo, aleat)


    def ajustarTamanyo(self, grafo):
        grados = sorted(grafo.degree())
        mayor = round(np.percentile(grados, 75))
        media = round(np.percentile(grados, 50))
        menor = round(np.percentile(grados, 25))

        for v in VertexSeq(grafo):
            if v.degree() > mayor:
                v['size'] = 60
            elif v.degree() > media:
                v['size'] = 40
            elif v.degree() > menor:
                v['size'] = 25
            else:
                v['size'] = 15

## Ejecutamos el algoritmo
ejec = algoritmoBarabasi()
ejec.main()
