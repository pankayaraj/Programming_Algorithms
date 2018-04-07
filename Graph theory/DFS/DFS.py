#1
def dfs(graph,start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
            
    return visited

#2
def dfs(graph, start, visited = None):
    if visited == None:
        visited = set()
    visited.add(start)
    for i in graph[start] - visited:
        dfs[graph,i,visited]
    return visited
