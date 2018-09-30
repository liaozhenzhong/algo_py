import random
from heap import *
from common import *

def test_build_heap():
    X = [Node(i) for i in reversed(range(10))]
    h = Heap(X, 'min')
    h.build_heap()
    [i.key for i in X] == [0, 1, 3, 2, 5, 4, 7, 9, 6, 8]

    X = [Node(i) for i in range(10)]
    h = Heap(X, 'max')
    h.build_heap()
    [i.key for i in X] == [9, 8, 6, 7, 4, 5, 2, 0, 3, 1]

def test_update_key():
    X = [Node(i) for i in range(10)]
    h = Heap(X, 'min')
    h.build_heap()
    h.update_key(9, 100)
    assert [i.key for i in X] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    h.update_key(9, -1)
    assert [i.key for i in X] == [-1, 0, 2, 3, 1, 5, 6, 7, 8, 4]
