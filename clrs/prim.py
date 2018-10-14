import math
from common import *
from heap import *

def prim(E, V):
    for node in V.values():
        node.prev = None
        node.key = math.inf
        node.color = Color.WHITE

    random_key = list(V.keys())[0]
    V[random_key].key = 0
    V[random_key].color = Color.BLACK
    h = Heap(list(V.values()), 'min')
    while not h.empty():
        node = h.extract()
        for nbr_value, weight in E[node.value].items():
            if V[nbr_value].color is Color.BLACK:
                continue
            if V[nbr_value].key > weight:
                h.update_key(V[nbr_value].pos, weight)
                V[nbr_value].prev = node
            node.color = Color.BLACK

    overall_weight = 0
    minimum_edges = []
    for node in V.values():
        if node.prev is None:
            continue
        overall_weight += node.key
        minimum_edges.append([node, node.prev])
    return overall_weight, minimum_edges
