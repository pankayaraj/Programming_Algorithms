#FORD-FULKERSON ALGORITHM for maximum flow form a source(s) to a sink(t)
# According to maxflow - mincut therom : maximum flow form a source to a sink in a flow-network is equall to
#                        minimum cut of the network( the total minimum capacity of edges that will disconnect the s and t)

#BFS is used
#Time complexity = O(VE^2) E = edges V = vertices | O(E*no of argumented paths)

#ALGORITHM IDEA REFERENCE : https://www.youtube.com/watch?v=GiN3jRdgxU4


from collections import defaultdict


class Graph():

    def __init__(self):
        self.structure = defaultdict(list)
        self.edges = {}

    def add_edges(self,from_node,to_node,flow_capacity):
        residual_capacity = flow_capacity        
        self.structure[from_node].append(to_node)
        self.structure[to_node].append(from_node)
        self.edges[(from_node,to_node)] = [flow_capacity,residual_capacity]
        if (to_node,from_node) not in self.edges:
            self.edges[(to_node,from_node)] = [0,0]
        


        
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
    edges = graph.edges
    visited = set([source])

    stack = [source]
    
    path_tracker = {}
    while stack:
        
        a_node = stack.pop()
        
        for i in set(structure[a_node]) - visited:
            if i != target:
                if edges[(a_node,i)][1] != 0:
                    path_tracker[i] = a_node
                    visited.add(i)
                    stack.append(i)
            else:
                if edges[(a_node,i)][1] != 0:
                    path_tracker[i] = a_node                    
                    return return_path(path_tracker,source,target)
    else:
        return -1


def ford_fulkerson(graph,source,sink):
    edges = graph.edges

    max_flow = 0
    arg_path = []
    arg_path = DFS(graph, source, sink)
    while arg_path != -1:
                
        #print arg_path
        
        possible_flow = float('inf')
        for i in xrange(len(arg_path)-1):
            edge = (arg_path[i],arg_path[i+1])
            current_flow = edges[edge][1]
            if current_flow < possible_flow:
                possible_flow = current_flow
           
        max_flow += possible_flow
        for i in xrange(len(arg_path)-1):
            edge1 = (arg_path[i],arg_path[i+1])
            edge2  = (arg_path[i+1],arg_path[i])
            edges[edge1][1] -= possible_flow
            edges[edge2][1] += possible_flow
        arg_path = DFS(graph, source, sink)
    return max_flow

# EXAMPLE 1: FROM:
#https://www.youtube.com/watch?v=GiN3jRdgxU4

'''
G = Graph()
G.add_edges('A','B',3)
G.add_edges('E','B',1)
G.add_edges('A','D',3)
G.add_edges('D','E',2)
G.add_edges('D','F',6)
G.add_edges('F','G',9)
G.add_edges('E','G',1)
G.add_edges('C','A',3)
G.add_edges('B','C',4)
G.add_edges('C','D',1)
G.add_edges('C','E',2)


#print DFS(G,'A','G')            
print ford_fulkerson(G,'A','G')
'''
# EXAMPLE 2: FROM:
#http://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
'''
G = Graph()
G.add_edges(0,1,16)
G.add_edges(0,2,13)
G.add_edges(1,2,10)
G.add_edges(2,1,4)
G.add_edges(1,3,12)
G.add_edges(2,4,14)
G.add_edges(3,2,9)
G.add_edges(4,3,7)
G.add_edges(3,5,20)
G.add_edges(4,5,4)
print ford_fulkerson(G,0,5)
'''

