# Maximum matching algorithm on bipartie graphs using Ford fulkerson algorithm DFS
# Here from node belongs to a certain biparte ste and to nodes beli=ong to another so make the input that way


from collections import defaultdict


class Graph():

    def __init__(self):
        self.structure = defaultdict(list)
        self.edges = {}
        self.edgelist = []
        self.source = 'Source'
        self.sink  = 'Sink'

    def add_edges(self,from_node,to_node):
                
        self.structure[from_node].append(to_node)
        self.structure[to_node].append(from_node)
        self.edges[(from_node,to_node)] = [1,1]
        if (to_node,from_node) not in self.edges:
            self.edges[(to_node,from_node)] = [0,0]
        self.edges[(self.source, from_node)] = [1,1]
        self.edges[(from_node, self.source)] = [0,0]
        self.edges[(to_node,self.sink)] = [1,1]
        self.edges[(self.sink,to_node)] = [0,0]
        self.structure[self.sink].append(to_node)
        self.structure[to_node].append(self.sink)
        self.structure[from_node].append(self.source)
        self.structure[self.source].append(from_node)
        self.edgelist.append((from_node,to_node))


    
def BFS_shortestpath_for_a_node(graph, source, target):
    visited = set([source])
    structure = graph.structure
    path_tracker = {}
    queue = [source]
    edges= graph.edges

    while queue:
        #print queue
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
            a_list = list(set(structure[a_node])-visited)
            for i in a_list:
                if edges[(a_node,i)][1] != 0:
                    path_tracker[i] = a_node
                    queue.append(i)
                    visited.add(i)
    else:
        return -1


def ford_fulkerson(graph):
    edgelist = graph.edgelist
    source = graph.source
    sink = graph.sink
    edges = graph.edges

    max_flow = 0
    arg_path = []
    arg_path = BFS_shortestpath_for_a_node(graph, source, sink)
    while arg_path != -1:
                
        print arg_path
        
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
        arg_path = BFS_shortestpath_for_a_node(graph, source, sink)

    matching = []
    if edgelist != []:
        for i in edgelist:
            
            if edges[i][1] == 0:
                matching.append(i)
    return max_flow, matching



G = Graph()




G.add_edges('1','B')
G.add_edges('1','C')
G.add_edges('2','A')
G.add_edges('2','C')
G.add_edges('3','B')
G.add_edges('3','D')
G.add_edges('4','B')
G.add_edges('4','C')
G.add_edges('5','D')
G.add_edges('5','E')

print ford_fulkerson(G)








        
    
