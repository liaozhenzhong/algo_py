from heap import *
from common import *

def dijkstra(E, V, root):
    h = Heap(list(V.values()), 'min')
    root.key = 0
    h.build_heap()
    while not h.empty():
        node = h.extract()
        for nbr_value, weight in E[node.value].items():
            if V[nbr_value].color is Color.BLACK:
                continue
            new_key = node.key + weight
            if new_key < V[nbr_value].key:
                h.update_key(V[nbr_value].pos, new_key)
                V[nbr_value].prev = node
            V[node.value].color = Color.BLACK

