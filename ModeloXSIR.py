#!/usr/bin/python
# -*- coding: latin-1 -*-
from ModeloCompartimental import ModeloCompartimental
from FuncionesAuxiliares import muestraAleatoria
from igraph import mean
import random as random


class ModeloXSIR(ModeloCompartimental):
    """ Modelo epidemiologico SIR para redes, con un nuevo estado
     de inmunes que llamaremos X. """

    def __init__(self, graph, beta=0.1, gamma=0.2):
        """ Construye el modelo compartimental sobre el
        grafo que recibe como argumento, y le asigna los
        valores de transicion. """
        ModeloCompartimental.__init__(self, graph, "XSIR")
        self.beta = float(beta)
        self.gamma = float(gamma)

    def reset(self):
        """ Inicializamos toda la poblacion a susceptibles """
        vs = xrange(self.grafo.vcount())
        self.compartimentos.move_vertices(vs, "X")

    def step(self):
        """" Un paso del modelo XSIR que es lo mismo que de SIR"""
        ## Extendemos la infeccion desde los nodos infectados
        for v in self.compartimentos["I"].copy():
            neis = self.grafo.neighbors(v)
            ## Algunos nodos se infectan
            for nei in muestraAleatoria(neis, self.beta):
                if self.compartimentos.get_state(nei) == "S":
                    self.compartimentos.move_vertice(nei, "I")

        ## Algunos se recuperan
        i_to_r = muestraAleatoria(self.compartimentos["I"], self.gamma)
        print self.compartimentos["I"]
        print "i_to_r"
        print i_to_r
        self.compartimentos.move_vertices(i_to_r, "R")

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
            s_to_i.update([nodo for nodo in neis if
                           self.grafo.vs[nodo].degree() > g_medio])
            ## Aplicamos los cambios
        self.compartimentos.move_vertices(s_to_i, "I")

        ## Algunos se recuperan
        i_to_r = muestraAleatoria(self.compartimentos["I"], self.gamma)
        self.compartimentos.move_vertices(i_to_r, "R")

    def stepInteligente2(self, beta):
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
            s_to_i.update([nodo for nodo in neis if
                           ((self.grafo.vs[nodo].degree() < g_medio) and
                            (random.random() < beta))])
            ## Aplicamos los cambios
        self.compartimentos.move_vertices(s_to_i, "I")

        ## Algunos se recuperan
        i_to_r = muestraAleatoria(self.compartimentos["I"], self.gamma)
        self.compartimentos.move_vertices(i_to_r, "R")
