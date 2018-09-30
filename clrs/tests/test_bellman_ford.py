from bellman_ford import *
from common import *

def test_bellman_ford():
    E = {
            's':{'t':3, 'y':5},
            't':{'y':2, 'x':6},
            'x':{'z':11},
            'y':{'t':1, 'z':6},
            'z':{'s':3, 'x':7},
            }
    V = {c:Node(key=math.inf, value=c) for c in E.keys()}
    bellman_ford(E, V, V['s'])
    
    for node in V.values():
        print(node.value, node.key, 
                node.prev.value if node.prev is not None else 'None')

    assert V['z'].key == 11
