from CompartmentalModel import CompartmentalModel
from codigo import sample

class SIRModel(CompartmentalModel):
    """SIR epidemic model for networks."""
    def __init__(self, graph, beta=0.1, gamma=0.2):
        """Constructs a SIR model on the given 'graph' with
        infection rate 'beta' and recovery rate 'gamma'."""
        CompartmentalModel.__init__(self, graph, "SIR")
        self.beta = float(beta)
        self.gamma = float(gamma)

    def reset(self):
        """All individuals susceptible"""
        vs = xrange(self.graph.vcount())
        self.compartments.move_vertices(vs, "S")

    def step(self):
        """Runs a single step of the SIR model simulation."""
        ## Contagious vertices spread the infection
        for vertex in self.compartments["I"].copy():
            neis = self.graph.neighbors(vertex)
            ## We may infect susceptible neighbors only
            for nei in sample(neis, self.beta):
                if self.compartments.get_state(nei) == "S":
                    self.compartments.move_vertex(nei, "I")

        ## Algunos se recuperan
        i_to_r = sample(self.compartments["I"], self.gamma)
        self.compartments.move_vertices(i_to_r, "R")
                    
