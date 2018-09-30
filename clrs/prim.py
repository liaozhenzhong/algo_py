import math
from heap import *

def prim(E, V):
    for node in V.values():
        node.prev = None
        node.key = math.inf

    Q = [node for node in V.values()]
    Q[0].key = 0
    h = Heap(Q, 'min')
    while not h.empty():
        node = h.extract()
        for nbr_value, weight in E[node.value].items():
            if V[nbr_value].key > weight:
                nbr_index = h.indexof(V[nbr_value])
                if nbr_index is None:
                    continue
                h.update_key(nbr_index, weight)
                V[nbr_value].prev = node

    overall_weight = 0
    minimum_edges = []
    for node in V.values():
        if node.prev is None:
            continue
        overall_weight += node.key
        minimum_edges.append([node, node.prev])
    return overall_weight, minimum_edges
