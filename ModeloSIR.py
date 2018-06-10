from ModeloCompartimental import ModeloCompartimental
from FuncionesAuxiliares import muestraAleatoria

class ModeloSIR(ModeloCompartimental):
    """Modelo epidemiologico SIR para redes"""
    def __init__(self, graph, beta=0.1, gamma=0.2):
        """Construye el modelo compartimental sobre el
        grafo que recibe como argumento, y le asigna los
        valores de transicion."""
        ModeloCompartimental.__init__(self, graph, "SIR")
        self.beta = float(beta)
        self.gamma = float(gamma)

    def reset(self):
        """Inicializamos toda la poblacion a susceptibles"""
        vs = xrange(self.grafo.vcount())
        self.compartimentos.move_vertices(vs, "S")

    def step(self):
        """Runs a single step of the SIR model simulation."""
        ## Extendemos la infeccion desde los nodos infectados
        for v in self.compartimentos["I"].copy():
            neis = self.grafo.neighbors(v)
            ## Algunos nodos se infectan
            for nei in muestraAleatoria(neis, self.beta):
                if self.compartimentos.get_state(nei) == "S":
                    self.compartimentos.move_vertex(nei, "I")

        ## Algunos se recuperan
        i_to_r = muestraAleatoria(self.compartimentos["I"], self.gamma)
        self.compartments.move_vertices(i_to_r, "R")
                    
