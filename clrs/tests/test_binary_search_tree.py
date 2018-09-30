import pytest
from common import *
from binary_search_tree import *


@pytest.fixture
def tree():
    t = BinarySearchTree()
    for i in [3, 1, 5, 0, 2, 4, 6]:
        t.insert(Node(i))
    return t

def test_add(tree):
    assert [0, 1, 2, 3, 4, 5, 6] == [i.key for i in tree.walk_inorder(tree.root)]

def test_search(tree):
    assert tree.search(-1) is None
    assert tree.search(1).key == 1

def test_min(tree):
    assert tree.min(tree.root).key == 0
    assert tree.min(tree.search(5)).key == 4

def test_max(tree):
    assert tree.max(tree.root).key == 6
    assert tree.max(tree.search(1)).key == 2

def test_successor(tree):
    for i in range(6):
        assert tree.successor(tree.search(i)).key == i + 1

def test_predecessor(tree):
    for i in range(6):
        assert tree.predecessor(tree.search(i+1)).key == i

def test_delete(tree):
    for i in range(7):
        node = tree.search(i)
        if node is not None:
            tree.delete(node)
