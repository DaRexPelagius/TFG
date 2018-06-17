import random
from igraph import *
import pylab


class FuncionesNucleo():

    def generaGrafo(self, tipo, n=10000, conectado=True, p=0.25):
        if tipo == "Erdos_Renyi":
            # Erdos_Renyi(n, p, m, directed=False, loops=False)
            # n = n vertices, p = probabilidad de aristas
            # (si hay p, no hay m)
            # m = numero de aristas
            grafo = Graph.Erdos_Renyi(n, m=2 * n)
        elif tipo == "Lattice":
            # Lattice(dim, nei=1, directed=False, mutual=True, circular=True)
            # dim = lista con las diemnsiones del grafo(sqrst(n) * sqrt(n)
            # en este caso)
            # nei = distancia a la que dos vertices estan conectados
            dim = [int(n ** 0.5), int(n ** 0.5)]
            grafo = Graph.Lattice(dim)
        elif tipo == "Grafo_Aleatorio":
            #
            r = 2 / ((n - 1) * pi) ** 0.5
            grafo = Graph.GRG(n, r)
        elif tipo == "Scale_Free":
            # Barabasi(n, m, outpref=False, directed=False, power=1,
            # zero_appeal=1, implementation="psumtree", start_from=None)
            # n = n vertices, m = numero de aristas de saldia en cada nodo,
            # o una lista con todas las aristas power = constante de
            # potencia, sino se especifica linear
            grafo = Graph.Barabasi(n, 2, power=2.2)
        elif tipo == "Small_Worlds":
            # Watts_Strogatz(dim, size, nei, p, loops=False, multiple=False)
            # Watts_Strogats parte de un grafo tipo Laticce
            # dim = dimensiones del lattice, size = tamanyo de todas
            # las dimensiones
            # nei = distancia a la que dos vertices estan conectados
            # p = rewiring probability
            grafo = Graph.Watts_Strogatz(1, n, 2, p)
        else:
            raise ValueError("No soportamos ese tipo de grafo.")

        # Comprobamos que el grafo este conectado, sino lo conectamos
        # nosotros
        if conectado and not grafo.is_connected():
            grafo = grafo.clusters().giant()
        return grafo

    def simulacion(self, modelo, tipo_grafo, tam_grafo=10000, infectados=1,
                   susceptibles=10000, runs=10, time=100, *args, **kwds):

        results = []
        # los susceptibles estan por defecto con 10000 para igualar
        # el tamanyo del grafo por defecto. Por tanto
        if susceptibles == 10000:
            susceptibles = tam_grafo
        for i in xrange(runs):
            current_run = []

            ## Inicializamos grafo y modelo
            grafo = self.generaGrafo(tipo_grafo, n=tam_grafo)
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

    def simulacionHub(self, modelo, tipo_grafo, tam_grafo=10000, num_infectados=1,
                      susceptibles=10000, runs=10, time=100, *args, **kwds):
        """ Simulacion"""

        results = []
        # los susceptibles estan por defecto con 10000 para igualar
        # el tamanyo del grafo por defecto. Por tanto
        if susceptibles == 10000:
            susceptibles = tam_grafo

        for i in xrange(runs):
            current_run = []
            n_infectados = num_infectados
            print "Ronda %d" % i

            ## Inicializamos grafo y modelo
            grafo = self.generaGrafo(tipo_grafo, n=tam_grafo)
            model = modelo(grafo, *args, **kwds)

            if susceptibles != tam_grafo:
                s = random.sample(range(grafo.vcount()), susceptibles)
                model.compartimentos.move_vertices(s, "S")

            ## Infectamos el numero de nodos indicado
            hubs = []
            infectados = []

            j = 0
            while n_infectados > len(hubs):
                for v in grafo.vs.select(_degree=(grafo.maxdegree() - j)):
                    hubs.append(v.index)
                if len(hubs) == 1:
                    infectados.append(hubs[0])
                else:
                    if len(hubs) > n_infectados:
                        print "[A]"
                        infectados = infectados + random.sample(hubs,
                                                                n_infectados)
                        print infectados
                    else:
                        infectados = infectados + random.sample(hubs, len(hubs))
                n_infectados = n_infectados - len(hubs)
                j += 1
            print infectados
            model.compartimentos.move_vertices(infectados, "I")

            # realizamos los pasos
            for t in xrange(time):
                model.step()
                p_infectados = model.compartimentos.tam_relativo("I")
                current_run.append(p_infectados)

            results.append(current_run)
        return results

    def simulacionAntiHub(self, modelo, tipo_grafo, tam_grafo=10000,
                          n_infectados=1, susceptibles=10000, runs=10, time=100,
                          *args, **kwds):
        """ Simulacion"""

        results = []
        # los susceptibles estan por defecto con 10000 para igualar
        # el tamanyo del grafo por defecto. Por tanto
        if susceptibles == 10000:
            susceptibles = tam_grafo

        for i in xrange(runs):
            print "Ronda %d" % i
            current_run = []

            ## Inicializamos grafo y modelo
            grafo = self.generaGrafo(tipo_grafo, n=tam_grafo)
            model = modelo(grafo, *args, **kwds)

            if susceptibles != tam_grafo:
                s = random.sample(range(grafo.vcount()), susceptibles)
                model.compartimentos.move_vertices(s, "S")

            ## Infectamos el numero de nodos indicado
            hubs = []
            infectados = []

            j = 1
            while n_infectados > len(hubs):
                for v in grafo.vs.select(_degree=j):
                    hubs.append(v.index)
                if len(hubs) == 1:
                    infectados.append(hubs[0])
                else:
                    if len(hubs) > n_infectados:
                        infectados = infectados + random.sample(hubs,
                                                                n_infectados)
                    else:
                        infectados = infectados + random.sample(hubs, len(hubs))
                n_infectados = n_infectados - len(hubs)
                j += 1

            model.compartimentos.move_vertices(infectados, "I")

            # realizamos los pasos
            for t in xrange(time):
                model.step()
                p_infectados = model.compartimentos.tam_relativo("I")
                current_run.append(p_infectados)

            results.append(current_run)
        return results

    def simulacionInteligente(self, modelo, tipo_grafo, tam_grafo=10000,
                              infectados=1, susceptibles=10000, runs=10,
                              time=100, *args, **kwds):
        results = []
        for i in xrange(runs):
            current_run = []

            ## Inicializamos grafo y modelo
            grafo = self.generaGrafo(tipo_grafo, n=tam_grafo)
            model = modelo(grafo, *args, **kwds)

            if susceptibles != tam_grafo:
                s = random.sample(range(grafo.vcount()), susceptibles)
                model.compartimentos.move_vertices(s, "S")
            ## Infectamos el numero de nodos indicado
            infectados = random.sample(range(grafo.vcount()), infectados)
            for i in infectados:
                # Comprobamos que son susceptibles
                if model.compartimentos.get_state(i) == "S":
                    model.compartimentos.move_vertice(i, "I")

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

    def simulacionInteligente2(self, modelo, tipo_grafo, tam_grafo=10000,
                               n_infectados=1, susceptibles=10000, runs=10,
                               time=100, beta=0.3, *args, **kwds):
        results = []
        if susceptibles == 10000:
            susceptibles = tam_grafo
        for i in xrange(runs):
            current_run = []

            ## Inicializamos grafo y modelo
            grafo = self.generaGrafo(tipo_grafo, n=tam_grafo)
            model = modelo(grafo, *args, **kwds)

            if susceptibles != tam_grafo:
                s = random.sample(range(grafo.vcount()), susceptibles)
                model.compartimentos.move_vertices(s, "S")
            ## Infectamos el numero de nodos indicado
            print "Vertices grafo: %d" % grafo.vcount()
            print "Infectados: %d" % n_infectados
            infectados = random.sample(range(grafo.vcount()), n_infectados)
            for i in infectados:
                # Comprobamos que son susceptibles
                if model.compartimentos.get_state(i) == "S":
                    model.compartimentos.move_vertice(i, "I")

            ## realizamos los pasos
            for t in xrange(time):
                model.stepInteligente2(beta)
                p_infectados = model.compartimentos.tam_relativo("I")
                current_run.append(p_infectados)

            results.append(current_run)
        return results

    def simulacionColores(self, modelo, tipo_grafo, tam_grafo=10000,
                               n_infectados=1, susceptibles=10000, runs=10,
                               time=100, beta=0.3, *args, **kwds):
        results = []
        if susceptibles == 10000:
            susceptibles = tam_grafo
        for i in xrange(runs):
            current_run = []

            ## Inicializamos grafo y modelo
            grafo = self.generaGrafo(tipo_grafo, n=tam_grafo)
            model = modelo(grafo, *args, **kwds)

            ## Infectamos el numero de nodos indicado
            if susceptibles != tam_grafo:
                s = random.sample(range(grafo.vcount()), int(susceptibles))
                model.compartimentos.move_vertices(s, "S")
            ## Infectamos el numero de nodos indicado
            infectados = random.sample(range(grafo.vcount()), n_infectados)
            for i in infectados:
                # Comprobamos que son susceptibles
                if model.compartimentos.get_state(i) == "S":
                    model.compartimentos.move_vertice(i, "I")

            ## Marcamos los pacientes cero en negro
            for id in model.compartimentos.compartimentos['I']:
                grafo.vs[id]['color'] = 'black'

            ## realizamos los pasos
            for t in xrange(7):
                model.step()
                if (t % 2) == 0:
                    for id in model.compartimentos.compartimentos['X']:
                        grafo.vs[id]['color'] = 'grey'
                    for id in model.compartimentos.compartimentos['S']:
                        grafo.vs[id]['color'] = 'yellow'
                    for id in model.compartimentos.compartimentos['I']:
                        if grafo.vs[id]['color'] != 'black':
                            grafo.vs[id]['color'] = 'red'
                    for id in model.compartimentos.compartimentos['R']:
                        grafo.vs[id]['color'] = 'green'
                    fichero = "simulacion5_" + "%d" % t + ".png"
                    plot(grafo, fichero)

            model.beta = 0.7
            model.gamma = 0.5

            ## realizamos los pasos
            for t in xrange(8,15):
                model.step()
                if (t % 2) == 0:
                    for id in model.compartimentos.compartimentos['X']:
                        grafo.vs[id]['color'] = 'grey'
                    for id in model.compartimentos.compartimentos['S']:
                        grafo.vs[id]['color'] = 'yellow'
                    for id in model.compartimentos.compartimentos['I']:
                        if grafo.vs[id]['color'] != 'black':
                            grafo.vs[id]['color'] = 'red'
                    for id in model.compartimentos.compartimentos['R']:
                        grafo.vs[id]['color'] = 'green'
                    fichero = "Figuras/simulacion5_" + "%d" % t + ".png"
                    plot(grafo, fichero)



        return results

    def simulacionGrupoInicial(self, modelo, tipo_grafo, tam_grafo=10000,
                               n_infectados=1, susceptibles=10000, runs=10,
                               time=100, *args, **kwds):
        """ Funcion simulacion adaptada, para que el grupo inicial de
        infectados sean vecinos. """

        results = []
        # los susceptibles estan por defecto con 10000 para igualar
        # el tamanyo del grafo por defecto. Por tanto
        if susceptibles == 10000:
            susceptibles = tam_grafo
        for i in xrange(runs):
            current_run = []

            # Inicializamos grafo y modelo
            grafo = self.generaGrafo(tipo_grafo, n=tam_grafo)
            model = modelo(grafo, *args, **kwds)

            if susceptibles != tam_grafo:
                s = random.sample(range(grafo.vcount()), int(susceptibles))
                model.compartimentos.move_vertices(s, "S")

            # Infectamos el numero de nodos indicado
            infectados = random.random(range(grafo.vcount()))
            for i in infectados:
                # Comprobamos que son susceptibles
                if model.compartimentos.get_state(i) == "S":
                    model.compartimentos.move_vertice(i, "I")

            ## realizamos los pasos
            for t in xrange(time):
                model.step()
                p_infectados = model.compartimentos.tam_relativo("I")
                current_run.append(p_infectados)

            results.append(current_run)
            return results

    def plot_results(self, results, color):
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

    def hallarUmbralCritico(self, modelo, tipo, betas, *args, **kwds):
        for beta in betas:
            results = self.simulacion(modelo, tipo, 100, beta=beta, *args,
                                      **kwds)
            self.plot_results(results, 'r-o')
            pylab.show()
            media = mean(run[-1] for run in results)
            print("Beta: %.2f  Media: %.4f" % (beta, media))
