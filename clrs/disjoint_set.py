def union(node1, node2):
    root1 = find_set(node1)
    root2 = find_set(node2)
    if root1 is root2:
        return
    if root1.rank > root2.rank:
        root2.parent = root1
    else:
        root1.parent = root2

def find_set(node):
    if node.parent is node:
        return node
    node.parent = find_set(node.parent)
    return node.parent

def make_set(node):
    node.parent = node
    return node
