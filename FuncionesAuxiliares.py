import random

def muestraAleatoria(nodos, p):
    """Funcion que permite seleccionar unos nodos de forma
    aleatorio para simular la transicion de estados en los
    distintos modelos, para ello usa la libreria random"""
    return [nodo for nodo in nodos if random.random() < p]