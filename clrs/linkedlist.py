from common import *

class DoubleLinkedList(object):
    def __init__(self):
        self.nil = Node(0)
        self.nil.prev = self.nil
        self.nil.next = self.nil

    def insert(self, node):
        a = self.nil
        b = self.nil.next
        node.prev = a
        node.next = b
        a.next = node
        b.prev = node

    def search(self, key):
        n = self.nil.next
        while n is not self.nil:
            if n.key == key:
                return n
            else:
                n = n.next
        return None

    def delete(self, node):
        a = node.prev
        b = node.next
        a.next = b
        b.prev = a

    def data(self):
        keys = []
        n = self.nil.next
        while n is not self.nil:
            keys.append(n.key)
            n = n.next

        return keys

