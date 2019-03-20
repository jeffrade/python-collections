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
    data = [
        Node("A", ["B", "C"]),
        Node("B", ["A", "D", "E"]),
        Node("C", ["A", "E", "F"]),
        Node("D", ["B", "G"]),
        Node("E", ["B", "C", "G"]),
        Node("F", ["C", "G"]),
        Node("G", ["D", "E", "F"])
    ]
    d.find("A", "G", data)


class Dijkstra():

    def find(self, start, end, data):
        shortest_path = []
        print("Starting at point {}".format(start))
        print("Looking for shortest path to point {}...".format(end))
        #TODO
        print("Done. Shortest path is {}".format(shortest_path))

        return shortest_path


class Node:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors


if __name__ == "__main__":
    main(sys.argv[1:])