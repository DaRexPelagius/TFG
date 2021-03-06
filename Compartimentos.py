""" Interfaz para los compartimentos del modelo"""
class Compartimentos(object):
    def __init__(self, grafo, comps):
        """ Mediante un grafo y los codigos de los compartimentos, comps,
        crea los compartimentos del modelo."""
        self.comps = list(comps)
        self.n = grafo.vcount()

        first_comp = self.comps[0]
        self.states = [first_comp] * self.n

        self.compartimentos = dict()
        for code in comps:
            self.compartimentos[code] = set()
        self.compartimentos[first_comp].update(xrange(self.n))


    def __getitem__(self, comp):
        """Devuelve el compartimento asociado
        al codigo comp."""
        
        return self.compartimentos[comp]

    def get_state(self, vertice):
        """Devuelve el codigo del compartimento
        en el que se encuentra el vertice."""
        return self.states[vertice]

    def move_vertice(self, vertice, comp):
        """Cambia el vertice de compartimento"""
        self.compartimentos[self.states[vertice]].remove(vertice)
        self.states[vertice] = comp
        self.compartimentos[comp].add(vertice)

    def move_vertices(self, vertices, code):
        """ Moves multiple vertices from their current compartment
        to another one."""
        for vertex in vertices:
            self.move_vertice(vertex, code)

    def tam_relativo(self, code):
        """ Returns the relative size of the compartment with
        the given 'code'."""
        return len(self.compartimentos[code]) / float(self.n)


    
