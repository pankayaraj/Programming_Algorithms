# DFS for finding the path from a node to another
# Using mapping

from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = []
        self.structure = defaultdict(list)

    def add_edge(self,from_node,to_node):
        self.structure[from_node].append(to_node)
        # If the graph is directed ignore the last line
        self.structure[to_node].append(from_node)

    def add_node(self,node):
        self.nodes.append(node)
        
def return_path(path_tracker,source,target):
    path = []
    c_node = target
    while c_node != source:
        path.append(c_node)
        c_node = path_tracker[c_node]
    else:
        path.append(c_node)
    path.reverse()
    return path

def DFS(graph,source,target):
    structure = graph.structure
    nodes = graph.nodes
    visited = set([source])

    stack = [source]
    
    path_tracker = {}
    while stack:
        
        a_node = stack.pop()
        for i in set(structure[a_node]) - visited:
            if i != target:
                path_tracker[i] = a_node
                visited.add(i)
                stack.append(i)
            else:
                path_tracker[i] = a_node
                visited.add(i)
                return return_path(path_tracker,source,target)
        else:
            return -1

'''
G = Graph()

for i in xrange(1,5):
    G.add_node(i)
G.add_edge(1,2)
G.add_edge(1,4)
G.add_edge(2,3)
G.add_edge(4,3)


print DFS(G,1,4)
    
'''


G = Graph()
for i in 'ABCDEFG':
    G.add_node(i)

G.add_edge('A','B')
G.add_edge('A','C')
G.add_edge('B','D')
G.add_edge('B','E')
G.add_edge('E','F')
G.add_edge('C','F')

print DFS(G,'A',"D")
         
