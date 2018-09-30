from strongly_connected_component import *
from common import *

def test_calc_connected_components():
    E = {
            'a':['e'],
            'b':['a'],
            'c':['b', 'd'],
            'd':['c'],
            'e':['b'],
            'f':['e', 'b', 'g'],
            'g':['f', 'c'],
            'h':['g', 'd', 'h'],
            }
    V = {c:Node(key=None, value=c) for c in E.keys()}
    component_collection = calc_connected_components(E, V)
    assert component_collection == [['h'], ['f', 'g'], ['c', 'd'], ['a', 'b', 'e']]
