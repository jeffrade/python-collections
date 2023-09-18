#!/usr/bin/env python3

# Implementation of Dijkstra's Algorithm
# Fastest path is: A -> C-> F -> G => 11
# Greedy implementation is: A -> B -> D -> G => 12
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
        shortest_path = [start]
        search_path_queue = deque()
        shortest_cost_path_map = {}
        nodes_visted = set()
        current_distance = 0

        print("Starting at point {}".format(start))
        print("Looking for shortest path to point {}...".format(end))

        shortest_cost_path_map[start] = float(0)
        all_nodes = sorted(list(data.keys()))
        start_index = all_nodes.index(start)
        end_index = all_nodes.index(end)
        nodes_to_search = all_nodes[start_index:end_index + 1]
        search_path_queue.append(start)
        shortest_cost_path_map[start] = 0
        print("nodes_to_search is {}".format(nodes_to_search))
        print("search_path_queue is {}".format(search_path_queue))
        while len(search_path_queue) > 0:
            print("Searching...")
            node = search_path_queue.pop()
            if node in nodes_visted:
                continue
            nodes_visted.add(node)
            print("Next node to search is {}...".format(node))
            if node == end:
                print("We've reached node {}.".format(node))
                break
            if node != start:
                shortest_cost_path_map[node] = float("inf")
            neighbors = list(data.get(node))
            lowest_neighbor_cost = float("inf")
            lowest_neighbor_name = None
            print("neighbors are {}...".format(neighbors))
            while len(neighbors) > 0:
                neighbor = neighbors.pop().popitem()
                print("Looking at neighbor {}...".format(neighbor))
                neighbor_name = neighbor[0]
                neighbor_cost = neighbor[1]
                if neighbor_name in nodes_visted:
                    continue
                print("Appending left neighbor {}.".format(neighbor_name))
                search_path_queue.appendleft(neighbor_name)
                if neighbor_cost < lowest_neighbor_cost:
                    lowest_neighbor_cost = neighbor_cost
                    lowest_neighbor_name = neighbor_name
            if lowest_neighbor_name != start:
                print("Appending neighbor {} since they are the shortest.".format(lowest_neighbor_name))
                search_path_queue.remove(lowest_neighbor_name)
                search_path_queue.append(lowest_neighbor_name)
                shortest_path.append(lowest_neighbor_name)
            current_distance += lowest_neighbor_cost
            print("current_distance is {}".format(current_distance))


        print("#########################################")
        print("shortest_cost_path_map is {}".format(shortest_cost_path_map))
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("current_distance is {}".format(current_distance))
        print("#########################################")
        print("Done. Shortest path is {}".format(shortest_path))
        return shortest_path


if __name__ == "__main__":
    main(sys.argv[1:])