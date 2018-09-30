from disjoint_set import *

def kruskal(E, V):
    for node in V.values():
        make_set(node)

    flat_E = []
    for start, ends in E.items():
        for end, weight in ends.items():
            flat_E.append([weight, start, end])
    E = sorted(flat_E)
    overall_weight = 0
    minimum_edges = []
    for weight, start, end in E:
        a = find_set(V[start])
        b = find_set(V[end])
        if a is not b:
            union(a, b)
            overall_weight += weight
            minimum_edges.append((a, b))

    return overall_weight, minimum_edges

