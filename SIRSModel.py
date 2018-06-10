from SIRModel import SIRModel
from codigo import sample

class SIRSModel(SIRModel):
    """SIR epidemic model for networks."""
    def __init__(self, graph, beta=0.1, gamma=0.2, lambda_=0.4):
        SIRModel.__init__(self, graph, beta, gamma)
        self.lambda_ = float(lambda_)


    def step(self):
        """Respecto al SIR solo incluye un paso mas donde los
        recuperados pueden pasar a ser susceptibles."""
        r_to_s = sample(self.compartments["R"], self.lambda_)
        self.compartments.move_vertices(r_to_s, "S")
        ## Ahora llamamos al SIR
        SIRModel.step(self)
