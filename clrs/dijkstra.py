from heap import *

def dijkstra(E, V, root):
    Q = [node for node in V.values()]
    h = Heap(Q, 'min')
    root.key = 0
    h.build_heap()
    while not h.empty():
        node = h.extract()
        for nbr_value, weight in E[node.value].items():
            new_key = node.key + weight
            if V[nbr_value].key > new_key:
                nbr_index = h.indexof(V[nbr_value])
                h.update_key(nbr_index, new_key)
                V[nbr_value].prev = node

