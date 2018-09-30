import random
from order import *
from common import *

def test_nth_order():
    for _ in range(100):
        X = list(range(10))
        random.shuffle(X)
        X = [Node(i) for i in X]
        index = random.randrange(0, 10)
        assert index == find_nth_order(X, index).key
