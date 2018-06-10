

# CLASE PAGINA 172
class Compartments(object):
    def __init__(self, graph, codes):
        """Creates a set of compartments for the vertices of
        the given 'graph'. The list of compartment codes is
        provided by 'codes'.

        Initially, all the vertices will be in the first
        compartment."""
        self.codes = list(codes)
        self.n = graph.vcount()

        first_comp = self.codes[0]
        self.states = [first_comp] * self.n

        self.compartments = dict()
        for code in codes:
            self.compartments[code] = set()
        self.compartments[first_comp].update(xrange(self.n))


    def __getitem__(self, code):
        """Returns the compartment corresponding to the given
        compartment 'code.'"""
        return self.compartments[code]

    def get_state(self, vertex):
        """Returns the state of the given 'vertex' (i.e. the
        code of its compartment.)"""
        return self.states[vertex]

    def move_vertex(self, vertex, code):
        """Moves the vertex from its current compartment to
        another one."""
        self.compartments[self.states[vertex]].remove(vertex)
        self.states[vertex] = code
        self.compartments[code].add(vertex)

    def move_vertices(self, vertices, code):
        """ Moves multiple vertices from their current compartment
        to another one."""
        for vertex in vertices:
            self.move_vertex(vertex, code)

    def relative_size(self, code):
        """ Returns the relative size of the compartment with
        the given 'code'."""
        return len(self.compartments[code]) / float(self.n)

#graph = Graph.GRG(100, 0.25)
#compartments = Compartments(graph, "SIR")

    
