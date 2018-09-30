def find_nth_order(X, nth):
    pivit = X[0]
    left = []
    right = []
    for i in range(1, len(X)):
        if X[i].key < pivit.key:
            left.append(X[i])
        else:
            right.append(X[i])
    if len(left) == nth:
        return pivit
    elif len(left) > nth:
        return find_nth_order(left, nth)
    else:
        return find_nth_order(right, nth-len(left)-1)
