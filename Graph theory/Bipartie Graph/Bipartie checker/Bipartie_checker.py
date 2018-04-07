#using colouring nodes this function names nodes using BFS
# In case of appliing on an already defined graph class insert the  colour dictionary
# reference : http://www.geeksforgeeks.org/bipartite-graph/
# Complexity O(n)

from collections import defaultdict


class Graph():
    def __init__(self):
        
        self.visited = set([])
        self.structure = defaultdict(set)
        self.colour = {}
    def add_edges(self,from_node,to_node):
        self.structure[from_node].add(to_node)
        #incase of bidirected graphs
        self.structure[to_node].add(from_node)

    def def_node(self,node):
        self.colour[node] = None
        
        
    
def bipartite(graph):
    
    
    structure = graph.structure
    visited = graph.visited
    queue = [structure.keys()[0]]
    statement = True
    visited = set([])
    colour_dict = graph.colour
    colour = 'blue'
    while queue:        
        
        if colour != 'blue':
            colour = 'blue'
        else:
            colour = 'red'
        
        for _ in xrange(len(queue)):
                       
            node = queue.pop(0)
            
            visited.add(node)
            
            queue.extend(list(structure[node]-visited))
                
                
            if colour_dict[node] != colour:
                colour_dict[node] = colour
            else:
                statement = False
                break
            
            
                
        if statement == False:
            break
    
    return statement

'''    
G = Graph()


for i in xrange(1,7):
    G.def_node(i)

G.add_edges(1,2)
G.add_edges(1,3)
G.add_edges(2,4)
G.add_edges(4,5)
G.add_edges(5,3)

print bipartite(G)
    
'''        
        
