
def dfs_path(graph,start,goal):
    stack = [(start,[start])]
    while stack:
        [vertex, path] = stack.pop()
        for nexte in graph[vertex]-set(path):
            if nexte == goal:
                yield path + [nexte]
            else:
                stack.append((nexte, path + [nexte]))

