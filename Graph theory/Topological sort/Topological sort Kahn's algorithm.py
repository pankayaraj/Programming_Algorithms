#Topologicall sort khan's algorithm
#works only strictly on DAG(directed acyclic graphs)
#1 can be used to calculate the dependency of vertices on another
#2 also  can be used to calculate the shortest distance of directed graphs
#What to do
    #1 add the nodes
    #2 create the structure
    #3 if it is a weighted graph turn the function into a compatible on using tuples
    # this function returns one of the possible   topological order
from collections import defaultdict


class Graph():
    def __init__(self):
        self.nodes = []
        self.structure = defaultdict(set)
        
    def add_edge(self,from_node,to_node):
        self.structure[from_node].add(to_node)

    def add_node(self,node):
        self.nodes.append(node)


def topological_sort(graph):

    nodes = graph.nodes
    visited = set([])
    structure = graph.structure
    sorted_stack = []
    
    

    while nodes:
        node = nodes[0]
        visited.add(node)
        stack = [node]
        while stack:
            
            a_node = stack[-1]
            visited.add(a_node)
            a_set = structure[a_node] - visited
            if len(a_set) == 0:
                sorted_stack.append(a_node)
                nodes.remove(a_node)
                stack.remove(a_node)
            stack.extend(list(structure[a_node]-visited))
    sorted_stack.reverse()
    return sorted_stack




        
        
        
        
    
