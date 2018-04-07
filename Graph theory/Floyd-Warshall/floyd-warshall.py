#Floyd-Warshall algorithm for findiing the shortest distance between every nodes of even a directed graph
#NOTE
# 1 if the graph is directed change the way of creating the graph by considering bidirected edges
# 2 function works even for negative values
# 3 get a way to display the nodes as numbers using a dictionary or etc coz it is easier for indexing
# 4 here the nodes alonng the rows are considered as the to nodes and the one along the cloumns are the from nodes. Distances are obtained at that basis
# 5 add the no of nodes when defining a graph from Graph class
# 6 if there is any error with the float conversion then define a value for inf
class Graph():
    def __init__(self,no_nodes):
        self.structure = [[float('inf')]*no_nodes for _ in xrange(no_nodes)]

    def add_node(self,from_node,to_node,distance):
        self.structure[from_node-1][to_node-1] = distance
        #self.structure[to_node-1][from_node-1] = distance 
        #just in case if the graph is bidirected


def floyd_warshall(graph,no_nodes):
    
    no_of_iterations = no_nodes
    structure = graph.structure
    # to make the distance from a node to that node 0 if there is any change make a change
    for node in xrange(no_of_iterations):
        structure[node][node] = 0
            
    for i in xrange(no_of_iterations):
        inter_node = i+1

        for f_node in xrange(no_of_iterations):
            for t_node in xrange(no_of_iterations):
                
                if structure[f_node][t_node] > structure[f_node][inter_node-1] + structure[inter_node-1][t_node]:
                    structure[f_node][t_node] = structure[f_node][inter_node-1] + structure[inter_node-1][t_node]
                else:
                    pass
    return structure


            
    
    
