# Implementation of Dijkstra's Algorithm

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

def start(start, end, data):
    print(start)

class Node:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors


data = {Node("A", None)}
start("A", "G", data)

print("Finish implementing this!")
