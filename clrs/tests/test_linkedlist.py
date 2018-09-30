import random
from linkedlist import *
from common import *

def test_insert():
    for _ in range(20):
        L = DoubleLinkedList()
        X = [random.randrange(0, 100) for _ in range(10)]
        for i in X:
            L.insert(Node(i))
        assert L.data() == list(reversed(X))

def test_search():
    for _ in range(20):
        L = DoubleLinkedList()
        X = [random.randrange(0, 100) for _ in range(10)]
        for i in X:
            L.insert(Node(i))
        index = random.randrange(0, len(X))
        assert L.search(X[index]).key == X[index]
