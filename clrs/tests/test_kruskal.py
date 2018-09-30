from kruskal import *
from common import *

def test_kruskal_min_span_tree():
    E = {
            'a': {'b': 4, 'h': 8},
            'c': {'b': 8, 'd': 7, 'f': 4},
            'd': {'f': 14},
            'e': {'d': 9, 'f': 10},
            'g': {'f': 2},
            'h': {'b': 11, 'g': 1, 'i': 7},
            'i': {'c': 2, 'g': 6},
            }

    V = set()
    for start, ends in E.items():
        for end, _ in ends.items():
            V.add(start)
            V.add(end)
    V = {c:Node(key=None, value=c) for c in V}
    overall_weight, minimum_edges = kruskal(E, V)
    assert overall_weight == 37

