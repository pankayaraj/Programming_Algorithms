
def bfs_path(graph,start,goal):
    queue = [(start,[start])]
    while queue:
        [vertex, path] = queue.pop(0)
        for nexte in graph[vertex]-set(path):
            if nexte == goal:
                yield path + [nexte]
            else:
                queue.append((nexte, path + [nexte]))
             

