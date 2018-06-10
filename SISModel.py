#!/usr/bin/python
# -*- coding: latin-1 -*-

from CompartmentalModel import CompartmentalModel
from codigo import sample

class SISModel(CompartmentalModel):
    """SIS modelo epidemiologico para redes"""

    def __init__(self, g, beta=0.1, gamma=0.2):
        """Creamos la clase que servirá de modelo"""
        CompartmentalModel.__init__(self, g, "SI")
        self.beta = float(beta)
        self.gamma = float(gamma)

    def reset(self):
        """Inicializamos todo el modelo a susceptibles"""
        vs = xrange(self.graph.vcount())
        self.compartments.move_vertices(vs, "S")

    def step(self):
        """ Un paso del modelo SIS"""
        ## Se extiende la infeccion
        s_to_i = set()# Inicializamos un conjunto para los traspasos

	## Calculamos para cada vértice infectado
	## Cuales de sus vecinos serán infectados
        for v in self.compartments["I"]:
            neis = self.graph.neighbors(v)
            s_to_i.update(sample(neis, self.beta))
	## Aplicamos los cambios
        self.compartments.move_vertices(s_to_i, "I")

        ## Algunos de los infectados se curarán
        i_to_s = sample(self.compartments["I"], self.gamma)
        self.compartments.move_vertices(i_to_s, "S")
                                    
