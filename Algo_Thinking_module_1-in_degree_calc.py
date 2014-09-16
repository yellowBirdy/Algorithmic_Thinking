#! /usr/bin/python

"""
This is mini project for Module 1 of Algorithmic Thinking 
course on Coursera from Rice Uni. 
The script calculates in-degree as well as in- degree dist
for digraphs represented by adjacency lists. It uses 3 test
digraphs and also introduces a function to generate a full graph

Added a function normalizing in_degree, and fixed in_degree calculating algorithm
Added a function prining the normalized in_degree distibution in log scale
"""
#imports
import matplotlib.pyplot as plt


EX_GRAPH0 = {0:set([1,2]),
             1:set(),
             2:set()}

EX_GRAPH1 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3]),
             3:set([0]),
             4:set([1]),
             5:set([2]),
             6:set()}

EX_GRAPH2 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3,7]),
             3:set([7]),
             4:set([1]),
             5:set([2]),
             6:set([]),
             7:set([3]),
             8:set([1,2]),
             9:set([0,3,4,5,6,7])}



def make_complete_graph(num_nodes) :
    """ 
    Generates a full digraph ("undigraph" as well in fact) 
    with num_nodes nodes for positive num_nodes otherwise generates 
    an empty graph. Uses adjacency list format ie. dictionary. 
    """

    the_graph = {}
    if num_nodes > 0 :  
        for vert in range(num_nodes):
            edges = set(range(vert)).union(set(range(vert+1,num_nodes)))
            the_graph[vert] = edges
    return the_graph

def compute_in_degrees(digraph):
    """ computes in degrees of each node of diagraph
    returns a dictionary with indegrees of each node """
    #initialize the in_degree
    in_degrees = {}
    for vert in digraph.keys():
        in_degrees[vert] = 0 
        
    for vert in digraph.keys():
        for in_vert in digraph[vert]:
            in_degrees[in_vert] += 1
               
    return in_degrees


def in_degree_distribution(digraph):
    """ computes distribution of in degrees of a digraph with aid 
    of compute_in_degree function """
    in_degr = compute_in_degrees(digraph)
    
    in_degree_dist = {}
    #uses set on the degrees to remove duplicates, sorting not needed as they 
    #will server as keys for a dictionary
    for degr in set(val for val in in_degr.values()):
        in_degree_dist[degr] = in_degr.values().count(degr) 
    
    return in_degree_dist


###code for normalization of degree distribution

def in_degree_distribution_normalized(digraph):
    """
    Calculates a normalized (ie. to relative frequecies) in_degree distribution of a digraph.
    by normalizing result of a call unnormalized degree distribtuion function.
    Takes a digraph defined as an adjacency list. 
    Returns a dictionary with relative frequecies of all degrees found in the input digraph
    """
    degree_distribution = in_degree_distribution(digraph)
    #calculate total count
    total_edges = 0.0
    for degree in degree_distribution.keys():
        total_edges += degree_distribution[degree]
    #normalize
    normalized_distribution = {}
    for degree in degree_distribution.keys():
        normalized_distribution[degree] = degree_distribution[degree]/total_edges
    
    return normalized_distribution

###code for printing the graph

def plot_indegree_distribution(in_degree_distribution):
    """
    plots a normalized empirical in_degree distribution in log scale(would plot any degree disto if lables and title changed)
    """
    plt.figure()
    plt.plot(in_degree_distribution.values(),in_degree_distribution.keys(),'ro')
    plt.xlabel ('Indegree of nodes (log)')
    plt.ylabel ('Relative frequency of Indegree (log)')
    plt.title ('Normlized Indegree Distibution in log/log scale')
    plt.grid(True)
    plt.yscale('log')
    plt.xscale('log')
    plt.show()

#####test
#print in_degree_distribution(EX_GRAPH1)

#plot_indegree_distribution (in_degree_distribution_normalized(EX_GRAPH2))