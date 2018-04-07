#Algorithm for finding the longest path in a DIRECTED ACYCLIC GRAPH
#Time Complexity O(V+E)

#Algoritthm for topological sorting

from collections import defaultdict


class Graph():
    def __init__(self):
        self.nodes = []
        self.structure = defaultdict(set)
        self.edges = {}
        
    def add_edge(self,from_node,to_node,distance):
        self.structure[from_node].add(to_node)
        self.edges[(from_node,to_node)] = distance

    def add_node(self,node):
        self.nodes.append(node)


def topological_sort(graph):

    nodes = graph.nodes
    nodes_main = []
    
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
                nodes_main.append(a_node)  # incase of multiple queries this makes the node list again since the node becomes empty in evry process of topological sort
                stack.remove(a_node)                        #as in the example in case of a  single qurey remove this and the one mentiones b elow as it consumes space
            stack.extend(list(structure[a_node]-visited))
    sorted_stack.reverse()
    graph.nodes = nodes_main # in the above said condition remove this as well
    return sorted_stack

def Longest_distance_path_for_DAG(graph,source,target= None):
    DISTANCE = {}
    Previous = {}
    nodes = graph.nodes
    edges = graph.edges
    
    for  i in nodes:
    
        if i != source:
            DISTANCE[i] = -float('inf')
            

        else:
            DISTANCE[i] = 0
            
    topological_order = topological_sort(graph)
    structure = graph.structure
          
    
    for  node  in topological_order:

        for node1 in structure[node]:
            
            if DISTANCE[node1] < DISTANCE[node] + edges[(node,node1)]:
                DISTANCE[node1] = DISTANCE[node] + edges[(node,node1)]
                Previous[node1] = node                                         # Avoid this as well 
    
    
    
    #------------------------------------------------------------------
    if target == None:
        return DISTANCE
    else:
        if DISTANCE[target] != -float('inf'):
            PATH = [target]
            x  =  target
            while True:
                if x !=  source:                                                # Incase if you don't need the path ignore this section 
                    PATH.append(Previous[x])                                    # and move on to the next comment and excecute it 
                    x = Previous[x]
                else:
                    
                    break
            PATH.reverse()   
            return  DISTANCE, PATH
        else:
            return DISTANCE, []
    #------------------------------------------------------------------
    #return DISTANCE
'''    
G = Graph()

for i in 'xyzsrt':
    
    G.add_node(i)

G.add_edge('t','x',7)
G.add_edge('r','t',3)
G.add_edge('t','y',4)
G.add_edge('s','t',2)
G.add_edge('t','z',2)
G.add_edge('x','y',-1)
G.add_edge('r','s',5)
G.add_edge('s','x',6)
G.add_edge('y','z',-2)
G.add_edge('x','z',1)
              
print Longest_distance_path_for_DAG(G,'s', 'r')
print Longest_distance_path_for_DAG(G,'s', 't')

print Longest_distance_path_for_DAG(G,'s', 'y')
print Longest_distance_path_for_DAG(G,'s', 'x')
print Longest_distance_path_for_DAG(G,'s', 'z')


'''












