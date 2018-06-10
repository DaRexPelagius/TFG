########### P.160 ###########
import plotly.plotly as py
import plotly.graph_objs as go
import igraph
from igraph import *
########### P.161 ###########
import random


# Primer bloque de codigo P.160
def create_tree(n, k):
	num_verttices = (k**n - 1) / (k - 1)
	return Graph.Tree(n, k, mode = "out")

#print create_tree(4, 2)

# Segundo bloque P.161
def sample(items, p):
    return [item for item in items if random.random() < p]

def simulate_infection(tree, p):
    ## Set all the vertices to healthy
    tree.vs["infected"] = False
    ## Infect the root vertex
    tree.vs[0]["infected"] = True
    ## Infected nodes propagate the infection downwards
    for vertex in tree.vs:
        if not vertex["infected"]:
            continue
        ## This is an infected node. Sample its successors
        ## uniformly with probability p and infect them
        neis = vertex.successors()
        for vertex in sample(neis, p):
            vertex["infected"] = True

# Paginas 161.162
def test_branching(n, k, p, num_trials=100):
    #Construct thre tree
    tree = create_tree(n, k)
    # Find the leaves(i.e. the last wave)
    leaves = tree.vs.select(_outdegree=0)
    print len(leaves)
    
    ## Run the trials and take the mean of the result
    result = RunningMean()
    for trial in xrange(num_trials):
        simulate_infection(tree, p)
        num_infected = len(leaves.select(infected=True))
        result.add(float(num_infected) / float(len(leaves)))
    return result.mean

# Primera prueba
##for i in xrange(11):
##    p = float(i) / 10.0
##    print "%.1f     %.3f" % (p, test_branching(12, 2, p))
##
##print "-----------------------------------------------------"

# Segunda prueba
##for i in xrange(11):
##    p = float(i) / 10.0
##    print "%.1f     %.3f" % (p, test_branching(8, 3, p))
