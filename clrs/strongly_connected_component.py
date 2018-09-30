from dfs import *

def transpose(E):
    ET = dict()
    for start, ends in E.items():
        for end in ends:
            if end not in ET:
                ET[end] = []
            ET[end].append(start)
    return ET

def calc_connected_components(E, V):
    ET = transpose(E)
    dfs = DFS(V)
    [_ for _ in dfs.depth_first_search(E, V, V['a'])]
    sorted_list = dfs.topological_order()
    dfs.reset(V)
    component_collection = []
    for node in sorted_list:
        if node.color == Color.WHITE:
            component_collection.append(
                    [i.value for i in dfs.start_with_this_node(ET, V, node)])
    return component_collection

