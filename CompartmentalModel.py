from Compartments import Compartments

class CompartmentalModel(object):
    """Abstract base class for compartmental epidemic
    models."""

    def __init__(self, graph, codes):
        """Creates a compartmental model associated to the given
        'graph'. 'codes' is a list that provides the comparment
        codes of the model."""
        self.graph = graph
        self.compartments = Compartments(graph, codes)
        self.reset()

    def relative_compartment_sizes(self):
        """Returns the relative sizes of each comparment in the
        model."""
        return [self.compartments.relative_size(code)
                for code in self.comparments.codes]

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
