import math

def dot(A, B):
    Ay = len(A)
    Ax = len(A[0])
    By = len(B)
    Bx = len(B[0])

    if Ax != By:
        return None

    C = [[0 for _ in range(Bx)] for _ in range(Ay)]

    for y in range(Ay):
        for x in range(Bx):
            for i in range(Ax):
                C[y][x] += (A[y][i] * B[i][x])
    return C

def min_chain_order(chain):
    L = len(chain)
    cost = [[math.inf]*L for _ in range(L)]
    order = [[0]*L for _ in range(L)]
    for i in range(L):
        cost[i][i] = chain[i]
    for i in range(1, L):
        cost[i-1][i] = 0

    for k in range(2, L):
        for x, y in zip(range(k, L), range(0, L-k)):
            for i in range(y+1, x):
                tmp = cost[y][i] + cost[i][x] + chain[y]*chain[x]*chain[i]
                if tmp < cost[y][x]:
                    cost[y][x] = tmp
                    order[y][x] = i
    return cost, order

def display_order(cost, order, y, x):
    if order[y][x] == 0:
        print('[{},{}]'.format(cost[y][x-1], cost[y+1][x]), end='')
        return
    print('(', end='')
    display_order(cost, order, y, order[y][x])
    display_order(cost, order, order[y][x], x)
    print(')', end='')
