import math
from dijkstra import *
from common import *

def test_dijkstra():
    E = {
            's':{'t':10, 'y':5},
            't':{'x':1, 'y':2},
            'x':{'z':4},
            'y':{'t':3, 'z':2, 'x':9},
            'z':{'s':7, 'x':6},
            }

    V = {c:Node(key=math.inf, value=c) for c in E.keys()}
    dijkstra(E, V, V['s'])
    for node in V.values():
        print(node.value, node.key)
    assert V['z'].key == 7
    assert V['z'].prev == V['y']
