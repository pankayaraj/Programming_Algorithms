#Bellman ford single source shortest path to the rest
#Dijkstra fails when there are negative edges. So in those cases bellman ford is used
#It is slower than dijkstra
#Time complexity: O(n*e) n = nodes, e = edges

#No need  to get the nodes in a numerical form unlike in floyd_warshall. Because dictionary is used

class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self,node):
        self.nodes.append(node)

    def add_edge(self,from_node,to_node,distance):
        self.edges.append((from_node,to_node,distance))
        #incase of bidirected edges
        #self.edges.append((to_node,from_node,distance))

def bellman_ford(graph,source):
    nodes = graph.nodes
    edges = graph.edges
    nodes_length = len(nodes)
    shortest_distance = {}
    for node in nodes:
        shortest_distance[node] = float('inf')
    shortest_distance[source] = 0

    for _ in xrange(nodes_length):
        for edge in edges:
            from_node,to_node,distance = edge
            if shortest_distance[from_node] == float('inf'):
                continue
            else:
                weight = shortest_distance[from_node] + distance
                if weight < shortest_distance[to_node]:
                    shortest_distance[to_node] = weight
    return shortest_distance
                


