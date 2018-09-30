import random
from hash import *
from common import *

def test_add():
    h = Hash(units=50)
    X = [random.randrange(0, 100) for _ in range(50)]
    for i in X:
        h.insert(Node(i))
    XX = h.data()
    assert sorted(X) == sorted(XX)


def test_delete():
    h = Hash(units=50)
    X = [random.randrange(0, 100) for _ in range(50)]
    for i in X:
        h.insert(Node(i))
    for i in X:
        h.delete(i)
    XX = h.data()
    assert len(XX) == 0

    h.delete(-1)
    XX = h.data()
    assert len(XX) == 0
