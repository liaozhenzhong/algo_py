from common import *

class DFS(object):
    def __init__(self, V):
        self.reset(V)

    def reset(self, V):
        self.time = 1
        self.topo = []
        for node in V.values():
            node.color = Color.WHITE
            node.start_time = 0
            node.end_time = 0

    def depth_first_search(self, E, V, root_node):
        if root_node.color == Color.WHITE:
            yield from self.start_with_this_node(E, V, root_node)
        for v in V.values():
            if v.color == Color.WHITE:
                yield from self.start_with_this_node(E, V, v)

    def start_with_this_node(self, E, V, node):
        node.color = Color.GRAY
        node.start_time = self.time
        self.time += 1
        yield node
        for nbr_value in E[node.value]:
            if V[nbr_value].color is Color.WHITE:
                yield from self.start_with_this_node(E, V, V[nbr_value])
        node.end_time = self.time
        self.time += 1
        self.topo.append(node)
        node.color = Color.BLACK

    def topological_order(self):
        return self.topo[::-1]
