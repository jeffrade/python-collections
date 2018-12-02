# Python 3.7.x or Python 2.7.x
# Breadth-first search shortest path from root node to given vertex,
# `graph` dictionary can have vertex values of [], None or not exist.

from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7, 8],
    5: [9, 10],
    6: None,
    7: [11, 12],
    11: [13]
}


def bfs(graph, start, end):
    visited = set()
    queue = deque()
    parent = {start: None}

    queue.append(start)
    while len(queue) > 0:
        node = queue.popleft()
        if node == end:
            return trav_shortest_path(start, end, parent)
        if node in visited:
            continue
        visited.add(node)

        children = graph.get(node, []) or []
        if len(children) == 0:
            continue
        for child in children:
            if child in visited:
                continue
            if child == node:
                continue
            queue.append(child)
            parent[child] = node

    return None


def trav_shortest_path(start, end, parent):
    shortest_path = [end]
    if start == end:
        return shortest_path
    step = parent.get(end)

    while step != start and step is not None:
        shortest_path.append(step)
        step = parent.get(step)

    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path


print("""
         1
       / | \ 
      2  3  4
    / |     | \ 
   5  6     7  8
 / |        | \ 
9  10       11 12 
            |
            13 
""")

path = bfs(graph, 1, 13)
print("1 -> 13 shortest path %s" % path)
path = bfs(graph, 2, 13)
print("2 -> 13 shortest path %s" % path)
path = bfs(graph, 3, 13)
print("3 -> 13 shortest path %s" % path)
path = bfs(graph, 4, 13)
print("4-> 13 shortest path %s" % path)
path = bfs(graph, 5, 13)
print("5-> 13 shortest path %s" % path)
path = bfs(graph, 6, 13)
print("6-> 13 shortest path %s" % path)
path = bfs(graph, 7, 13)
print("7-> 13 shortest path %s" % path)
path = bfs(graph, 8, 13)
print("8-> 13 shortest path %s" % path)
path = bfs(graph, 9, 13)
print("9-> 13 shortest path %s" % path)
path = bfs(graph, 10, 13)
print("10-> 13 shortest path %s" % path)
path = bfs(graph, 11, 13)
print("11-> 13 shortest path %s" % path)
path = bfs(graph, 12, 13)
print("12-> 13 shortest path %s" % path)
path = bfs(graph, 1, 10)
print("1-> 10 shortest path %s" % path)
path = bfs(graph, 2, 10)
print("2-> 10 shortest path %s" % path)
path = bfs(graph, 3, 10)
print("3-> 10 shortest path %s" % path)
path = bfs(graph, 4, 10)
print("4-> 10 shortest path %s" % path)
path = bfs(graph, 5, 10)
print("5-> 10 shortest path %s" % path)
path = bfs(graph, 6, 10)
print("6-> 10 shortest path %s" % path)
path = bfs(graph, 7, 10)
print("7-> 10 shortest path %s" % path)
path = bfs(graph, 8, 10)
print("8-> 10 shortest path %s" % path)
path = bfs(graph, 9, 10)
print("9-> 10 shortest path %s" % path)
path = bfs(graph, 10, 10)
print("10-> 10 shortest path %s" % path)
