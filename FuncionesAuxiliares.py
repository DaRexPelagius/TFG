import random
import igraph
from igraph import *
from SISModel import SISModel
#from SISWithImmunityModel import SISWithImmunityModel
import pylab
#from Inmunizadores import *
#from functools import partial


def muestraAleatoria(nodos, p):
    """Funcion que permite seleccionar unos nodos de forma
    aleatorio para simular la transicion de estados en los
    distintos modelos, para ello usa la libreria random"""
    return [nodo for nodo in nodos if random.random() < p]

## de mometno esta planeado para que tengas 4 aristas desde cada nodo
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
        dim = [int(n ** 0.5), int(n ** 0.5)]
        grafo = Graph.Watts_Strogatz(1, 100, 2, 0.25)
    else:
        raise ValueError("No soportamos ese tipo de grafo.")

    ## Comprobamos que el grafo este conectado, sino lo conectamos nosotros
    if conectado and not grafo.is_connected():
        grafo = grafo.clusters().giant()
    return grafo

def simulacion(modelo, tipo_grafo, tam_grafo=10000, hub=0, infectados=1, runs=10, time=100, *args, **kwds):
    """ Si hub = 0, la epidemia empieza un nodo aleatorio, si hub = 1 empieza en el nodo de mayor grado,
    si hub = 2, entonces empieza en un nodo de menor grado."""
    results = []
    for i in xrange(runs):
        current_run = []

        ## Inicializamos grafo y modelo
        grafo = generaGrafo(tipo_grafo, n = tam_grafo)        
        model = modelo(grafo, *args, **kwds)
        
        ## Infectamos el numero de nodos indicado
        if hub == 0:
            infectados = random.sample(range(grafo.vcount()), infectados)
        elif hub == 1:
            ## Buscamos el nodo de mayor grado
            infectados = list()
            infectados.append(grafo.vs.select(_degree = grafo.maxdegree())[0].index)
        elif hub == 2:
            ## Buscamos un nodo de grado 2
            infectados = list()
            infectados.append(grafo.vs.select(_degree = 4)[0].index)
            
        model.compartments.move_vertices(infectados, "I")

        ## realizamos los pasos
        for t in xrange(time):
            model.step()
            frac_infected = model.compartments.relative_size("I")
            current_run.append(frac_infected)

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

def simularScaleFree(n, beta, gamma=0.25, epsilon=0.01):
    grafo = Graph.Barabasi(n, 3)
    modelo = SISModel(grafo, beta=beta, gamma=gamma)

    ## Aqui infecta la mita de ordenadores
    infectados = random.sample(range(n), n // 2)
    modelo.compartments.move_vertices(infectados, "I")

    rm = RunningMean()
    while len(rm) == 0 or rm.sd > epsilon:
        rm.clear()
        for i in xrange(100):
            modelo.step()
            rm.add(modelo.compartments.relative_size("I"))
    return rm.mean

def multiPasoSF(n, beta, gamma=0.25, epsilon=1, runs=10):
    results = []
    for i in xrange(runs):
        frac = simularScaleFree(n, beta, gamma, epsilon)
        results.append(frac)
    return mean(results)

def sf_prevalence_plot(phi_for_n):
    gamma = 0.25
    args = []
    symbols = ('b+', 'gs', 'rx', 'co', 'mD')
    plot = []
    for idx, n  in enumerate(sorted(phi_for_n.keys())):
        xs, ys = [], []
        for phi in phi_for_n[n]:
            beta = gamma / phi
            frac = multiPasoSF(n, beta, gamma)
            xs.append(phi)
            ys.append(frac)
        args.extend(xs, ys, symbols[idx])

    pylab.plot(*args)
    pylab.show()

#def test_immunizer(immunizer):
#    for modelo in ("Erdos_Renyi", "Scale_Free"):
#        resultados = simulacion(SISWithImmunityModel, modelo,\
#                                time=100, num_infected=10, immunizer=immunizer,\
#                                beta=0.25, gamma=0.25)
#        print("%s: %.4f" % (modelo, results[0][-1]))

## prueba inmunizador
#immunizer = partial(random_immunizer, m=2000)
#test_immunizer(immunizer)



# Probando a ver
#resultados = simulacion(SISModel, "Lattice", beta=0.25, gamma=0.25,time=600, hub=2)
#plot_results(resultados, 'r-o')
#pylab.show()
####
##g = generaGrafo("Scale_Free", n = 50)
##plot(g, "scalefree.png")
##
##
##g2 = generaGrafo("Small_Worlds", n = 50)
##plot(g2, "smallworlds.png")

##betas = [0.06, 0.07, 0.08, 0.09, 0.10]
##hallarUmbralCritico(SISModel, "Erdos_Renyi", betas, gamma=0.25, time=600)

##print multiPasoSF(10000, 0.05)



#### Prueba rara para scale free
##phi_for_n = dict()
##phi_for_n[100000] = [7.5, 8, 10]
##phi_for_n[500000] = [9, 9.5, 10, 10.5, 11, 11.5]
##phi_for_n[1000000] = [8.5, 9, 9.5, 10, 10.5, 11, 11.5]
##phi_for_n[5000000] = [12, 13, 14, 15, 16]
##phi_for_n[8500000] = [18, 20]
##sf_prevalence_plot(phi_for_n)
