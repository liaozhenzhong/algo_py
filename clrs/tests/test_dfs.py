from dfs import *
from common import *

def test_dfs():
    E = {
            'u':['v', 'x'],
            'v':['y'],
            'w':['y', 'z'],
            'x':['v'],
            'y':['x'],
            'z':['z'],
            }
    V = {c:Node(key=None, value=c) for c in E.keys()}
    
    dfs = DFS(V)
    assert ['u', 'v', 'y', 'x', 'w', 'z'] == [node.value for node in dfs.depth_first_search(E, V, V['u'])]

