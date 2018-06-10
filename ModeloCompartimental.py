from Compartimentos import Compartimentos

class ModeloCompartimental(object):
    """Interfaz para la clase de los modelos
    epidemiologicos compartimentales."""

    def __init__(self, grafo, codes):
        """Inicializa un.modelo compartimental sobre un
        grafo que recibe como argumento y el codigo
        asociado a los compartimentos"""
        self.grafo = grafo
        self.compartimentos = Compartimentos(grafo, codes)
        self.reset()

    def tam_relativo_compartimentos(self):
        """Returns the relative sizes of each comparment in the
        model."""
        return [self.compartimentos.tam_relativo(cmp)
                for cmp in self.compartimentos.cmps]

    def reset(self):
        """Resets the compartments to an initial state. This
        method must be overriden in subclasses."""
        raise NotImplementedError

    def step(self):
        """ Implements the logic of the epidemic model. This method
        must be overriden by subclasses."""
        raise NotImplementedError

    def step_many(self, n):
        """Runs 'n' steps of the epidemic model at once by
        calling 'step' multiple times."""
        for i in xrange(n):
            self.step()
