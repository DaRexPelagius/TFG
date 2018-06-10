#!/usr/bin/python
# -*- coding: latin-1 -*-

import codigo
import Compartments
from SISModel import SISModel
from SIRModel import SIRModel
from SIRSModel import SIRSModel
import igraph
from igraph import *
import random
import pylab
import numpy as np

# Funcion para crear un grafo aleatorio
def generate_graph(n=1000):
    graph = Graph.Erdos_Renyi(n, m=2*n)
    if not graph.is_connected():
        graph = graph.clusters().giant()
    return graph

def simulate(model_class, runs=10, time=100, *args, **kwds):
    results = []
    for i in xrange(runs):
        current_run = []

        ## Inicializamos grafo y modelo
        graph = generate_graph()
        model = model_class(graph, *args, **kwds)

        ## Infectamos un nodo aleatorio
        v = random.choice(graph.vs)
        model.compartments.move_vertex(v.index, "I")

        ## realizamos los pasos
        for t in xrange(time):
            model.step()
            frac_infected = model.compartments.relative_size("I")
            current_run.append(frac_infected)

        results.append(current_run)
        return results


results = simulate(SISModel, beta=0.25, gamma=0.25)

def plot_results(results, color):
    ## Calculate the means for each time point
    averaged = [mean(items) for items in izip(*results)]

    ## Create the argument list for pylab.plot
    args = []
    for row in results:
        args += [row, 'k-']
    args += [averaged, color]

    ## Creathe the plot
    pylab.plot(*args)

##azul = 'b-o'
##plot_results(results, azul)
##
##cyan = 'c-o'
##results = simulate(SIRModel, beta=0.25, gamma=0.25)
##plot_results(results, cyan)
##
##
##rojo = 'r-o'
##results = simulate(SIRSModel, beta=0.25, gamma=0.25, lambda_=0.25)
##plot_results(results, rojo)
##
g = generate_graph(n=100)
g.clusters()
comms = g.community_multilevel() ## Esta funcion es de igraph saca las comunidades de un grafo
igraph.plot(comms, mark_groups = True)## mark_groups te crea un aura alrededor de las comunidades


##pylab.legends()

## Necesario para monstrar lo que se imprimio
#pylab.show()




# Cosas de la clase Grafo de iGraph
#http://igraph.org/python/doc/igraph.Graph-class.html
