
# coding: utf-8

## 1. Project

# In[42]:

"""
Project 2 of Algorythmic Thinking implementation: 
1. implementing BFS algorithm
2. computing CC of undirected graph using BFS algorithm
3. computing resilence of a network
"""

#import O(1) queue implementation
from collections import deque
import random


# In[43]:

#small fully connected graph
EX_UGRAPH0 = {0:set([1,2,3]),
              1:set([0,2]),
              2:set([0,1]),
              3:set([0])}

#small graph with 2 CC
EX_UGRAPH1 = {0:set([1,2,3]),
              1:set([0,2]),
              2:set([0,1]),
              3:set([0]),
              4:set([5]),
              5:set([4])}

#slightly bigge graph with 4 CC and largest CC size 5
EX_UGRAPH2 = {0:set([1,3,5]),
              1:set([0]),
              2:set([]),
              3:set([0,5]),
              4:set([7,8]),
              5:set([0,3,9]),
              6:set([]),
              7:set([4,8]),
              8:set([4,7]),
              9:set([5])
              }


### Task 1: BFS-Visited implementation

# In[44]:



def bfs_visited(ugraph, start_node):
    """
    Implementation of BFS-visited alogorithm 
    takes 2 args, undirected graph as adjacency list and the start node
    returns a set of all visited nodes - a connected component of the start node
    """
    queue = deque()
    visited = set()
    visited = visited | set([start_node])
    queue.append(start_node)
    while queue:
        #deque
        current_node = queue.popleft()
        for neighbour in ugraph[current_node]:
            if neighbour not in visited:
                visited = visited | set([neighbour])
                queue.append(neighbour)
    #end of queue
    return visited



### Task2: Computing a set of connected components CC using BFS-Visited

# In[45]:

def cc_visited(ugraph) :
    """ 
    computes all connected components using BFS-visited algorithm
    takes 1 arg: undirected graph as adjacency list
    Returns a list of all connected components of ugraph
    """
    remaining_nodes = set(ugraph.keys())
    connected_components = []
    while remaining_nodes:
        start_node = random.sample(remaining_nodes,1)[0]
        #computes connected component of start_node and adds it to the list of all connected components
        cc_of_start_node = bfs_visited(ugraph,start_node)
        connected_components.append(cc_of_start_node)
        #removes all nodes from computed connected component from remaining nodes
        remaining_nodes = remaining_nodes - cc_of_start_node
        
    return connected_components


def largest_cc_size(ugraph):
    """ 
    Computes the size of largest connected component of a ugraph
    takes 1 arg: undirected graph as adjacency list
    returns integer size of largest connected component
    """
    connected_components = cc_visited(ugraph)
    largest_cc = 0
    for component in connected_components:
        cc_size=len(component)
        if cc_size > largest_cc:
            largest_cc = cc_size
    
    return largest_cc
        


### Part3: Resilence test

# In[51]:

def compute_resilience(ugraph, attack_order):
    """
    Computes the size of largest connected component of a ugraph as a funcion of attacked nodes
    takes 2 args: undirected graph as adjacency list and a list of attacked nodes 
    returns a list of sizes of largest connected component, first elelment is for full network followed by size after noeds have been attacked
    """
    #copy graph  to local variable 
    local_ugraph = {node:graph[node] for node in graph}
    
    largest_cc = []
    largest_cc.append(largest_cc_size(local_ugraph))
    for attacked_node in attack_order:
        attacked_neighbors = local_ugraph[attacked_node]
        for neighbor in attacked_neighbors:
            local_ugraph[neighbor].remove(attacked_node)
        del local_ugraph[attacked_node]
        largest_cc.append(largest_cc_size(local_ugraph))
    
    return largest_cc
    

