#!/usr/bin/env python3
# Implementation of Dijkstra's Algorithm
import sys
from collections import deque

print("""
         A
        / \ 
       2   3
       |   |
       B   C
      / \ / \ 
     4  6 5  7
     |  | /  |
     D  E    F
     |  |   /
     6  5  1
      \ | /
        G

""")

def main(args):
    print(args)
    d = Dijkstra()
    data = {
        "A": [{"B": 2}, {"C": 3}],
        "B": [{"A": 2}, {"D": 4}, {"E": 6}],
        "C": [{"A": 3}, {"E": 5}, {"F": 7}],
        "D": [{"B": 4}, {"G": 6}],
        "E": [{"B": 6}, {"C": 5}, {"G": 5}],
        "F": [{"C": 7}, {"G": 1}],
        "G": [{"D": 6}, {"E": 5}, {"F": 1}]
    }
    d.find("A", "G", data)


class Dijkstra():

    def find(self, start, end, data):
        shortest_path = []
        search_path_queue = deque()
        shortest_cost_path_map = {}
        nodes_visted = set()
        current_distance = 0

        print("Starting at point {}".format(start))
        print("Looking for shortest path to point {}...".format(end))

        start_neighbors = list(data.get(start))
        nodes_visted.add(start)
        shortest_cost_path_map[start] = float(0)
        while len(start_neighbors) > 0:
            neighbor = start_neighbors.pop().popitem()
            search_path_queue.append(neighbor[0])

        # node: [{node: x}, {node: y}]
        all_nodes = sorted(list(data.keys()))
        start_index = all_nodes.index(start)
        end_index = all_nodes.index(end)
        nodes = all_nodes[start_index:end_index + 1]
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node in nodes_visted:
                continue
            nodes_visted.add(node)

            neighbors = list(data.get(node))
            shortest_cost_path_map[node] = float("inf")
            lowest_neighbor_cost = float("inf")
            while len(neighbors) > 0:
                neighbor = neighbors.pop().popitem()
                neighbor_name = neighbor[0]
                neighbor_cost = neighbor[1]
                if neighbor_cost < lowest_neighbor_cost:
                    lowest_neighbor_cost = neighbor_cost
                search_path_queue.append(neighbor_name)

            current_distance += lowest_neighbor_cost


        print("#########################################")
        print(search_path_queue)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(shortest_cost_path_map)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(current_distance)
        print("#########################################")
        print("Done. Shortest path is {}".format(shortest_path))
        return shortest_path


if __name__ == "__main__":
    main(sys.argv[1:])