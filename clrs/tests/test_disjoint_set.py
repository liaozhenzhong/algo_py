from disjoint_set import *
from common import *

def test_set():
    a = make_set(Node(1))
    b = make_set(Node(2))
    c = make_set(Node(3))
    d = make_set(Node(4))

    union(a, c)
    union(b, d)
    assert [3, 4, 3, 4] == [
            find_set(a).key,
            find_set(b).key,
            find_set(c).key,
            find_set(d).key,
            ]

    union(a, b)
    assert [4, 4, 4, 4] == [
            find_set(a).key,
            find_set(b).key,
            find_set(c).key,
            find_set(d).key,
            ]
