import math
from common import *

def bubble_sort(X):
    for i in reversed(range(len(X))):
        for j in range(i):
            if X[j].key > X[j+1].key:
                X[j], X[j+1] = X[j+1], X[j]

def insertion_sort(X):
    for i in range(1, len(X)):
        for j in reversed(range(i)):
            if X[j].key > X[j+1].key:
                X[j], X[j+1] = X[j+1], X[j]

def selection_sort(X):
    for i in range(len(X)):
        smallest = i
        for j in range(i, len(X)):
            if X[j].key < X[smallest].key:
                smallest = j
        X[i], X[smallest] = X[smallest], X[i]

def merge_sort(X):
    if len(X) < 2:
        return X

    left = merge_sort(X[:len(X)//2])
    right = merge_sort(X[len(X)//2:])

    left.append(Node(math.inf))
    right.append(Node(math.inf))

    new_X = []
    p_left, p_right = 0, 0
    for i in range(len(X)):
        if left[p_left].key < right[p_right].key:
            new_X.append(left[p_left])
            p_left += 1
        else:
            new_X.append(right[p_right])
            p_right += 1

    return new_X

def quick_sort(X):
    if len(X) < 2:
        return X

    left = []
    right = []
    for i in range(1, len(X)):
        if X[i].key < X[0].key:
            left.append(X[i])
        else:
            right.append(X[i])
    return quick_sort(left) + [X[0]] + quick_sort(right)

def counting_sort(X):
    if len(X) == 0:
        return
    move = min([node.key for node in X])
    for node in X:
        node.key -= move

    key_array = [node.key for node in X]
    maximum = max(key_array)

    counting_array = [0] * (maximum + 1)

    for key in key_array:
        counting_array[key] += 1

    for i in range(1, len(counting_array)):
        counting_array[i] += counting_array[i-1]

    new_X = [Node(0)] * (len(X) + 1)

    for i in reversed(range(len(X))):
        index_in_new_X = counting_array[X[i].key]
        new_X[index_in_new_X] = X[i]
        counting_array[X[i].key] -= 1

    for node in new_X:
        node.key += move

    X[:] = new_X[1:]

def radix_sort(X):
    if len(X) == 0:
        return

    max_num_len = len(str(max([node.key for node in X])))

    for node in X:
        node.key = str(node.key).zfill(max_num_len)

    for digit in reversed(range(max_num_len)):
        for i in range(1, len(X)):
            for j in reversed(range(i)):
                if X[j].key[digit] > X[j+1].key[digit]:
                    X[j], X[j+1] = X[j+1], X[j]
    for node in X:
        node.key = int(node.key)
