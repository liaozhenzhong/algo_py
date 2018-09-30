from bfs import *
from common import *

def test_bfs():
    E = {
            'r':['v', 's'],
            's':['r', 'w'],
            't':['w', 'x', 'u'],
            'u':['t', 'x', 'y'],
            'v':['r'],
            'w':['s', 't', 'x'],
            'x':['t', 'u', 'w', 'y'],
            'y':['x', 'u'],
            }
    V = {c:Node(key=None, value=c) for c in E.keys()}

    unvisited = Queue()
    V['s'].color = Color.GRAY
    unvisited.put(V['s'])
    assert ['r', 'w', 'v', 't', 'x', 'u', 'y'] == [node.value for node in breadth_first_search(E, V, unvisited)]
