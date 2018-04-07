# Enter your code here. Read input from STDIN. Print output to STDOUT
# Kruskal minimum spanning tree for weighted undirected graphs
# Source assistance :https://raw.githubusercontent.com/israelst/Algorithms-Book--Python/master/5-Greedy-algorithms/kruskal.py
# What to do
    #get the nodes in the node set
    #get the edeges in the edges set
    #use the main function
class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = set([])

    def add_node(self,node):
        self.nodes.append(node)

    def add_edge(self,from_node,to_node,distance):
        self.edges.add((distance,from_node,to_node))

parent = {} # a dictionary with nodes, when a node is accessed it woulf give it's parent at orign
rank = {} # a dictionary of nodes where  higher rank is assigned to the parent at the top

#function for initalizing the parent and rank dictionary
def form_set(nodes):
    for node in nodes:
        parent[node] = node
        rank[node] = 0

# A function which recursively calls itself to get the parent of the node at the tree's orign
def get_parent(node):
    
    if parent[node] != node:
        #recursively check until we get the foremost parent
        parent[node] = get_parent(parent[node])
    return parent[node]

def unite(node1,node2):
    #after the connectivity being checked in the main code join the two unconnected parent nodes to form a tree, same as joinnning the child nodes but makes the ranking easier
    root1 = get_parent(node1)
    root2 = get_parent(node2)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        #incase of an equal rank make the one an arbitary one as the parent
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(graph,parent,rank):
    nodes = graph.nodes
    edges = list(graph.edges)
    form_set(nodes)
    MST = []
    edges.sort()
    for edge in edges:
        distance,node1,node2 = edge
        if get_parent(node1) != get_parent(node2):
            unite(node1,node2)
            MST.append(edge)
    return MST
    

    
