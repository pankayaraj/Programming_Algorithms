from collections import defaultdict

class Graph():
    def __init__(self):
        self.structure = defaultdict(set)
        self.unvisited = set([])

    def add_edge(self,from_node,to_node):
        self.structure[from_node].add(to_node)
        self.structure[to_node].add(from_node)

    def add_node(self,node):
        self.unvisited.add(node)

def dfs_path(graph,source,destination):
    visited = []
    structure = graph.structure
    unvisited = graph.unvisited
    visited.append(source)
    a_node = source
    
    stack = []
    while len(unvisited) != 0:
        
        
        unvisited.remove(a_node)
        for node in structure[a_node]-set(visited):
            if node == destination:
                
                visited.append(node)
                path = [visited.pop()]
                j = 0
                for i in xrange(1,len(visited)+1):
                    
                    if visited[-i] in structure[path[j]]:
                        path.append(visited[-i])
                        j += 1
                        
                    else:
                        pass
                        
                path.reverse()
                return path
                                
                unvisited = set([])
            else:
                stack.append(node)
        a_node = stack.pop()
        visited.append(a_node)
    
            
            
            
        
        
