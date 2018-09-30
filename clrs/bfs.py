from queue import Queue
from common import *

def breadth_first_search(E, V, unvisited):
    new_unvisited = Queue()
    while not unvisited.empty():
        node = unvisited.get()
        for nbr_value in E[node.value]:
            if V[nbr_value].color is Color.WHITE:
                V[nbr_value].color = Color.GRAY
                yield V[nbr_value]
                new_unvisited.put(V[nbr_value])
        node.color = Color.BLACK
    if not new_unvisited.empty():
        yield from breadth_first_search(E, V, new_unvisited)
