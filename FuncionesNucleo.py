import random
from igraph import *
import pylab

def generaGrafo(tipo, n=10000, conectado=True):
    if tipo == "Erdos_Renyi":
        # Erdos_Renyi(n, p, m, directed=False, loops=False)
        # n = n vertices, p = probabilidad de aristas (si hay p, no hay m)
        # m = numero de aristas
        grafo = Graph.Erdos_Renyi(n, m = 2*n)
    elif tipo == "Lattice":
        #Lattice(dim, nei=1, directed=False, mutual=True, circular=True)
        #dim = lista con las diemnsiones del grafo(sqrst(n) * sqrt(n) en este caso)
        #nei = distancia a la que dos vertices estan conectados
        dim = [int(n ** 0.5), int(n ** 0.5)]
        grafo = Graph.Lattice(dim)
    elif tipo == "Grafo_Aleatorio":
        #
        r = 2 / ((n - 1) * pi) ** 0.5
        grafo = Graph.GRG(n, r)
    elif tipo == "Scale_Free":
        # Barabasi(n, m, outpref=False, directed=False, power=1,
        # zero_appeal=1, implementation="psumtree", start_from=None)
        # n = n vertices, m = numero de aristas de saldia en cada nodo, o
        # una lista con todas las aristas
        # power = constante de potencia, sino se especifica linear
        # zero_appeals... nada, implementation... nada
        grafo = Graph.Barabasi(n, 2)
    elif tipo == "Small_Worlds":
        # Watts_Strogatz(dim, size, nei, p, loops=False, multiple=False)
        # Watts_Strogats parte de un grafo tipo Laticce
        # dim = dimensiones del lattice, size = tamanyo de todas las dimensiones
        # nei = distancia a la que dos vertices estan conectados
        # p = rewiring probability
        grafo = Graph.Watts_Strogatz(1, n, 2, 0.25)
    else:
        raise ValueError("No soportamos ese tipo de grafo.")

    ## Comprobamos que el grafo este conectado, sino lo conectamos nosotros
    if conectado and not grafo.is_connected():
        grafo = grafo.clusters().giant()
    return grafo

def simulacion(modelo, tipo_grafo, tam_grafo=10000, hub=0, infectados=1, susceptibles = 10000, runs=10, time=100, *args, **kwds):
    """ Si hub = 0, la epidemia empieza un nodo aleatorio, si hub = 1 empieza en el nodo de mayor grado,
    si hub = 2, entonces empieza en un nodo de menor grado."""
    results = []
    if susceptibles == 10000:
        susceptibles = tam_grafo
    for i in xrange(runs):
        current_run = []

        ## Inicializamos grafo y modelo
        grafo = generaGrafo(tipo_grafo, n = tam_grafo)        
        model = modelo(grafo, *args, **kwds)

        if susceptibles != tam_grafo:
            s = random.sample(range(grafo.vcount()), susceptibles)
            model.compartimentos.move_vertices(s, "S")
        ## Infectamos el numero de nodos indicado
        infectados = random.sample(range(grafo.vcount()), infectados)
        model.compartimentos.move_vertices(infectados, "I")

        ## realizamos los pasos
        for t in xrange(time):
            model.step()
            p_infectados = model.compartimentos.tam_relativo("I")
            current_run.append(p_infectados)

        results.append(current_run)
        return results

def simulacionInteligente(modelo, tipo_grafo, tam_grafo=10000, hub=0, infectados=1, susceptibles = 10000, runs=10, time=100, *args, **kwds):

    results = []
    for i in xrange(runs):
        current_run = []

        ## Inicializamos grafo y modelo
        grafo = generaGrafo(tipo_grafo, n = tam_grafo)
        model = modelo(grafo, *args, **kwds)

        if susceptibles != tam_grafo:
            s = random.sample(range(grafo.vcount()), susceptibles)
            model.compartimentos.move_vertices(s, "S")
        ## Infectamos el numero de nodos indicado
        infectados = random.sample(range(grafo.vcount()), infectados)
        model.compartimentos.move_vertices(infectados, "I")

        ## realizamos los pasos
        for t in xrange(time):
            if t <= 5:
                model.stepInteligente()
            else:
                model.step()
            p_infectados = model.compartimentos.tam_relativo("I")
            current_run.append(p_infectados)

        results.append(current_run)
        return results

    def simulacionInteligente(modelo, tipo_grafo, tam_grafo=10000, hub=0, infectados=1, susceptibles=10000, runs=10,
                              time=100, *args, **kwds):

        results = []
        for i in xrange(runs):
            current_run = []

            ## Inicializamos grafo y modelo
            grafo = generaGrafo(tipo_grafo, n=tam_grafo)
            model = modelo(grafo, *args, **kwds)

            if susceptibles != tam_grafo:
                s = random.sample(range(grafo.vcount()), susceptibles)
                model.compartimentos.move_vertices(s, "S")
            ## Infectamos el numero de nodos indicado
            infectados = random.sample(range(grafo.vcount()), infectados)
            model.compartimentos.move_vertices(infectados, "I")

            ## realizamos los pasos
            for t in xrange(time):
                model.stepInteligente2()
                p_infectados = model.compartimentos.tam_relativo("I")
                current_run.append(p_infectados)

            results.append(current_run)
            return results


def simulacionInteligente2(modelo, tipo_grafo, tam_grafo=10000, hub=0, infectados=1, susceptibles = 10000, runs=10, time=100, *args, **kwds):
    results = []
    if susceptibles == 10000:
        susceptibles = tam_grafo
    for i in xrange(runs):
        current_run = []

        ## Inicializamos grafo y modelo
        grafo = generaGrafo(tipo_grafo, n = tam_grafo)
        model = modelo(grafo, *args, **kwds)

        if susceptibles != tam_grafo:
            s = random.sample(range(grafo.vcount()), susceptibles)
            model.compartimentos.move_vertices(s, "S")
        ## Infectamos el numero de nodos indicado
        infectados = random.sample(range(grafo.vcount()), infectados)
        model.compartimentos.move_vertices(infectados, "I")

        ## realizamos los pasos
        for t in xrange(time):
            model.stepInteligente2()
            p_infectados = model.compartimentos.tam_relativo("I")
            current_run.append(p_infectados)

        results.append(current_run)
        return results



def plot_results(results, color):
	for r in results:
		print r
		## Calculate the means for each time point
		averaged = [mean(items) for items in izip(*r)]

		## Create the argument list for pylab.plot
		args = []
		for row in r:
			args += [row, 'k-']
		args += [averaged, color]

		## Creathe the plot
		pylab.plot(*args)

def hallarUmbralCritico(modelo, tipo, betas, *args, **kwds):
    for beta in betas:
        results = simulacion(modelo, tipo, 100, beta=beta, *args, **kwds)
        plot_results(results, 'r-o')
        pylab.show()
        media = mean(run[-1] for run in results)
        print("Beta: %.2f  Media: %.4f" % (beta, media))
