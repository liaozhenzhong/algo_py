import math
from prim import *
from common import *

def test_prim_min_span_tree():
    E = {
            'a':{'b':4, 'h':8},
            'b':{'a':4, 'h':11, 'c':8},
            'c':{'b':8, 'i':2, 'f':4, 'd':7},
            'd':{'c':7, 'f':14, 'e':9},
            'e':{'d':9, 'f':10},
            'f':{'g':2, 'c':4, 'd':14, 'e':10},
            'g':{'h':1, 'i':6, 'f':2},
            'h':{'a':8, 'b':11, 'i':7, 'g':1},
            'i':{'c':2, 'g':6, 'h':7},
            }
    V = {c:Node(key=None, value=c) for c in E.keys()}
    overall_weight, minimum_edges = prim(E, V)
    assert overall_weight == 37
