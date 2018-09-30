import math
import random
from linkedlist import *


class Hash(object):
    def __init__(self, units):
        self.units = units
        self.table = [DoubleLinkedList() for _ in range(units)]

    def insert(self, node):
        hash_value = self.get_hash_value(node.key)
        self.table[hash_value].insert(node)

    def delete(self, key):
        hash_value = self.get_hash_value(key)
        target_node = self.table[hash_value].search(key)
        if target_node is not None:
            self.table[hash_value].delete(target_node)

    def search(self, key):
        hash_value = self.get_hash_value(key)
        return self.table[hash_value].search(key)

    def get_hash_value(self, key):
        return self.by_division(key)
        #return self.by_multiplication(key)

    def by_division(self, key):
        return key % self.units

    def by_multiplication(self, key):
        s = 2**64
        A = (math.sqrt(5)-1)/2
        val = int(key * s * A)
        val %= 10**14
        val //= 10**11
        return val % self.units

    def data(self):
        val = []
        for t in self.table:
            val += t.data()
        return val
