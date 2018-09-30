class Heap(object):
    def __init__(self, X, heap_type):
        self.X = X
        self.compare = self._lesser if heap_type == 'min' else self._greater_equal

    def _greater_equal(self, a, b):
        return a >= b

    def _lesser(self, a, b):
        return a < b

    def _left(self, i):
        return (i + 1)*2 - 1

    def _right(self, i):
        return (i + 1)*2

    def _parent(self, i):
        return (i - 1)//2

    def heapify(self, i):
        most_what = i
        left = self._left(i)
        right = self._right(i)
        if left < len(self.X) and self.compare(self.X[left].key, self.X[most_what].key):
            most_what = left
        if right < len(self.X) and self.compare(self.X[right].key, self.X[most_what].key):
            most_what = right
        if i != most_what:
            self.X[most_what], self.X[i] = self.X[i], self.X[most_what]
            self.heapify(most_what)

    def build_heap(self):
        for i in reversed(range(len(self.X)//2)):
            self.heapify(i)

    def extract(self):
        if self.empty():
            return None
        self.X[0], self.X[-1] = self.X[-1], self.X[0]
        node = self.X.pop()
        if not self.empty():
            self.heapify(0)

        return node

    def top(self):
        if self.empty():
            return None
        return self.X[0]

    def heap_sort(self):
        X = []
        while not self.empty():
            X.append(self.extract())
        return X

    def empty(self):
        return len(self.X) == 0

    def update_key(self, i, new_key):
        if self.compare(self.X[i].key, new_key):
            return
        self.X[i].key = new_key
        def _update(i):
            p = self._parent(i)
            if p < 0:
                return
            if self.compare(self.X[i].key, self.X[p].key):
                self.X[p], self.X[i] = self.X[i], self.X[p]
                _update(p)
        _update(i)

    def indexof(self, node):
        index = 0
        while index < len(self.X) and node is not self.X[index]:
            index += 1
        return index if index < len(self.X) else None
