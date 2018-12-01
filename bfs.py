# Python 3.7.x or Python 2.7.x
# Breadth-first search if path from a top node exists to nth child node

from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7, 8],
    5: [9, 10],
    7: [11, 12],
    11: [13]
}

def bfs(graph, start, end):
    visited = set()
    queue = deque()

    queue.append(start)
    while len(queue) > 0:
        node = queue.popleft()
        if node == end:
            return True
        if node in visited:
            continue
        visited.add(node)

        children = graph.get(node, [])
        if len(children) == 0:
            continue
        for child in children:
            if child in visited:
                continue
            if child == node:
                continue
            queue.append(child)

    return False

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
print("1 -> 13 ? %s" % path)
path = bfs(graph, 2, 13)
print("2 -> 13 ? %s" % path)
path = bfs(graph, 3, 13)
print("3 -> 13 ? %s" % path)
path = bfs(graph, 4, 13)
print("4-> 13 ? %s" % path)
path = bfs(graph, 5, 13)
print("5-> 13 ? %s" % path)
path = bfs(graph, 6, 13)
print("6-> 13 ? %s" % path)
path = bfs(graph, 7, 13)
print("7-> 13 ? %s" % path)
path = bfs(graph, 8, 13)
print("8-> 13 ? %s" % path)
path = bfs(graph, 9, 13)
print("9-> 13 ? %s" % path)
path = bfs(graph, 10, 13)
print("10-> 13 ? %s" % path)
path = bfs(graph, 11, 13)
print("11-> 13 ? %s" % path)
path = bfs(graph, 12, 13)
print("12-> 13 ? %s" % path)
