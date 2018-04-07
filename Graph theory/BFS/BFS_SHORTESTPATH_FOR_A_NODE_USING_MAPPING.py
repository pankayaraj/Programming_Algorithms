# BFS path finding algorithm
# shoortest path from a node to the other is found
#path is obtained by mapping each node to the one that introduced it to the queue(BACKTRACKING)

from collections import defaultdict


class Graph():
    def __init__(self):
        self.structure = defaultdict(set)
        self.path_tracker = {}

    def add_edge(self,from_node,to_node):
        self.structure[from_node].add(to_node)
        self.structure[to_node].add(from_node)


def BFS_shortestpath_for_a_node(graph, source, target):
    visited = set([source])
    structure = graph.structure
    path_tracker = graph.path_tracker
    queue = [source]

    while queue:
        
        a_node  = queue.pop(0)
        
        
        if a_node == target:
            path = [target]
            ans = None
            pointer = a_node
            
            while ans != source:
                ans = path_tracker[pointer]
                pointer = ans
                path.append(ans)
            
            path.reverse()
            return path
        else:
            a_list = list(structure[a_node]-visited)
            for i in a_list:
                path_tracker[i] = a_node
                visited.add(i)
                queue.append(i)
            
    else:
        return -1
'''
G = Graph()
G.add_edge('A','C')
G.add_edge('A','B')
G.add_edge('B','D')
G.add_edge('B','E')
G.add_edge('E','F')
G.add_edge('C','F')


print BFS_shortestpath_for_a_node(G,'A','F')
     
'''       
