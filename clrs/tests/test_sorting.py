import random
from sorting import *
from common import *

def data(l):
    X = [random.randrange(0, 100) for _ in range(l)]
    Y = sorted(X)
    X = [Node(i) for i in X]
    Y = [Node(i) for i in Y]
    return X, Y

def test_bubble_sort():
    for l in range(0, 10):
        for _ in range(20):
            X, Y = data(l)
            bubble_sort(X)
            assert [i.key for i in X] == [i.key for i in Y]

def test_insertion_sort():
    for l in range(0, 10):
        for _ in range(20):
            X, Y = data(l)
            insertion_sort(X)
            assert [i.key for i in X] == [i.key for i in Y]

def test_selection_sort():
    for l in range(0, 10):
        for _ in range(20):
            X, Y = data(l)
            selection_sort(X)
            assert [i.key for i in X] == [i.key for i in Y]

def test_merge_sort():
    for l in range(0, 10):
        for _ in range(20):
            X, Y = data(l)
            X = merge_sort(X)
            assert [i.key for i in X] == [i.key for i in Y]

def test_quick_sort():
    for l in range(0, 10):
        for _ in range(20):
            X, Y = data(l)
            X = quick_sort(X)
            assert [i.key for i in X] == [i.key for i in Y]

def test_counting_sort():
    for l in range(0, 10):
        for _ in range(20):
            X, Y = data(l)
            counting_sort(X)
            assert [i.key for i in X] == [i.key for i in Y]

def test_radix_sort():
    for l in range(0, 10):
        for _ in range(20):
            X, Y = data(l)
            radix_sort(X)
            assert [i.key for i in X] == [i.key for i in Y]
