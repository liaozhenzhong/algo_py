from dfs import *

def shortest_paths(E, V, root):
    dfs = DFS(V)
    [_ for _ in dfs.depth_first_search(E, V, root)]

    for node in dfs.topological_order():
        for end, weight in E[node.value].items():
            new_key = node.key + weight
            if new_key < V[end].key:
                V[end].key = new_key
                V[end].prev = node

