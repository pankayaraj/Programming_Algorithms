#Dijsktra for shortest path from a source in weighted bidirected grapths
# NOTE:
# Add nodes to nodes set
# create the normal graph structure within structure as tuples with edge and specific diatances
# shortes_distance dictionary presents with the shortest distance
from collections import defaultdict
class Graph:
    def __init__ (self):
        self.nodes = set([])
        self.graph_structure = defaultdict(list)
        self.shortest_distance = {}
        
    def add_node(self,node):
        self.nodes.add(node)

    def create_structure(self,from_node,to_node,distance):
        self.graph_structure[from_node].append((to_node,distance))
        self.graph_structure[to_node].append((from_node,distance))

def dijsktra(graph,source):
    nodes = graph.nodes
    structure = graph.graph_structure
    shortest_distance =  graph.shortest_distance
    
    for i in nodes:
        if i != source:
            shortest_distance[i] = float('inf')
        else:
            shortest_distance[i] = 0
    
    while nodes:
        min_value = None
        min_value_node = None
        for node in nodes:
            if min_value == None:
                min_value = shortest_distance[node]
                min_value_node = node
            else:
                if  min_value > shortest_distance[node]:
                    min_value = shortest_distance[node]
                    min_value_node = node

        if min_value == float('inf'):
            break
        else:
            nodes.remove(min_value_node)

            current_node_weight = min_value
            for (node,distance) in structure[min_value_node]:
                weight = current_node_weight + distance
                if weight < shortest_distance[node]:
                    shortest_distance[node] = weight
    return shortest_distance
            

    
            
