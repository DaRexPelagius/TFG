from ModeloSIR import ModeloSIR
from FuncionesAuxiliares import muestraAleatoria

class ModeloSIRS(ModeloSIR):
    """Modelo epidemiologico SIRS para redes. Esta clase
    extiende la del modelo SIR"""
    def __init__(self, graph, beta=0.1, gamma=0.2, lambda_=0.4):
        ModeloSIR.__init__(self, graph, beta, gamma)
        ## El nuevo valor de transicion entre
        ## recuperados y susceptibles
        self.lambda_ = float(lambda_)


    def step(self):
        """Respecto al SIR solo incluye un paso mas donde los
        recuperados pueden pasar a ser susceptibles."""
        r_to_s = muestraAleatoria(self.compartimentos["R"], self.lambda_)
        self.compartimentos.move_vertices(r_to_s, "S")
        ## Ahora llamamos al SIR
        ModeloSIR.step(self)
