import math
from matrix import *

def test_dot():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 10], [8, 11], [9, 12]]
    C = [[50, 68], [122, 167]]

    assert C == dot(A, B)


def test_chain_order():
    print()
    chain = [30, 35, 15, 5, 10, 20, 25]
    L = len(chain)
    X, order = min_chain_order(chain)
    for y in range(L):
        for x in range(L):
            if X[y][x] == math.inf:
                X[y][x] = 0
            print('%5d'%(X[y][x]), end=', ')
        print()
    print()
    for y in range(L):
        for x in range(L):
            print('%5d'%order[y][x], end=', ')
        print()
    display_order(X, order, 0, L-1)
