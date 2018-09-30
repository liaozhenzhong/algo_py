import math

def bellman_ford(E, V, root):
    root.key = 0
    for i in range(len(V)-1):
        for start, ends in E.items():
            for end, weight in ends.items():
                new_value = V[start].key + weight
                if new_value < V[end].key:
                    V[end].key = new_value
                    V[end].prev = V[start]
    for start, ends in E.items():
        for end, weight in ends.items():
            if V[start].key + weight < V[end].key:
                return False
    return True
