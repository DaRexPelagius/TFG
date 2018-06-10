#!/usr/bin/python
# -*- coding: latin-1 -*-

from ModeloCompartimental import ModeloCompartimental
from FuncionesAuxiliares import muestraAleatoria
from igraph import mean
import random as random

class ModeloSIS(ModeloCompartimental):
    """SIS modelo epidemiologico para redes"""

    def __init__(self, g, beta=0.1, gamma=0.2):
        """Creamos la clase que servirá de modelo"""
        ModeloCompartimental.__init__(self, g, "SI")
        self.beta = float(beta)
        self.gamma = float(gamma)

    def reset(self):
        """Inicializamos toda la poblacion a susceptibles"""
        vs = xrange(self.grafo.vcount())
        self.compartimentos.move_vertices(vs, "S")

    def step(self):
        """ Un paso del modelo SIS"""
        ## Se extiende la infeccion
        s_to_i = set()# Inicializamos un conjunto para los traspasos

	    ## Calculamos para cada vertice infectado
	    ## Cuales de sus vecinos seran infectados
        for v in self.compartimentos["I"]:
            neis = self.grafo.neighbors(v)
            s_to_i.update(muestraAleatoria(neis, self.beta))
	    ## Aplicamos los cambios
        self.compartimentos.move_vertices(s_to_i, "I")

        ## Algunos de los infectados se curaran
        i_to_s = muestraAleatoria(self.compartimentos["I"], self.gamma)
        self.compartimentos.move_vertices(i_to_s, "S")

    def stepInteligente(self):
        """ Un paso del modelo SIS en el que solo ataca nodos
        con un grado superior a la media."""
        ## Se extiende la infeccion
        s_to_i = set()  # Inicializamos un conjunto para los traspasos

        ## Grado medio del grafo
        g_medio = mean(self.grafo.degree()) // 1

        ## Calculamos para cada vertice infectado
        ## Cuales de sus vecinos seran infectados
        for v in self.compartimentos["I"]:
            neis = self.grafo.neighbors(v)
            s_to_i.update([nodo for nodo in neis if self.grafo.vs[nodo].degree() > g_medio])
            ## Aplicamos los cambios
        self.compartimentos.move_vertices(s_to_i, "I")

        ## Algunos de los infectados se curaran
        i_to_s = muestraAleatoria(self.compartimentos["I"], self.gamma)
        self.compartimentos.move_vertices(i_to_s, "S")

    def stepInteligente2(self):
        """ Un paso del modelo SIS en el que solo ataca nodos
        con un grado superior a la media."""
        ## Se extiende la infeccion
        s_to_i = set()  # Inicializamos un conjunto para los traspasos

        ## Grado medio del grafo
        g_medio = mean(self.grafo.degree()) // 1

        ## Calculamos para cada vertice infectado
        ## Cuales de sus vecinos seran infectados
        for v in self.compartimentos["I"]:
            neis = self.grafo.neighbors(v)
            s_to_i.update([nodo for nodo in neis if ((self.grafo.vs[nodo].degree() < g_medio) and \
                (random.random() < beta))])
            ## Aplicamos los cambios
        self.compartimentos.move_vertices(s_to_i, "I")

        ## Algunos de los infectados se curaran
        i_to_s = muestraAleatoria(self.compartimentos["I"], self.gamma)
        self.compartimentos.move_vertices(i_to_s, "S")
