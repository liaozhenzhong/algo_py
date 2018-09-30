from queue import Queue

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        def _insert(current_node, new_node):
            if new_node.key < current_node.key:
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                else:
                    _insert(current_node.left, new_node)
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                else:
                    _insert(current_node.right, new_node)

        if self.root is None:
            self.root = new_node
            return
        _insert(self.root, new_node)

    def walk_inorder(self, node):
        if node is None:
            return
        yield from self.walk_inorder(node.left)
        yield node
        yield from self.walk_inorder(node.right)

    def walk_preorder(self, node):
        if node is None:
            return
        yield node
        yield from self.walk_preorder(node.left)
        yield from self.walk_preorder(node.right)

    def walk_postorder(self, node):
        if node is None:
            return
        yield from self.walk_postorder(node.left)
        yield from self.walk_postorder(node.right)
        yield node

    def walk_queue(self, node):
        def _walk_queue(q):
            new_q = Queue()
            while not q.empty():
                n = q.get()
                yield n
                if n.left is not None:
                    new_q.put(n.left)
                if n.right is not None:
                    new_q.put(n.right)
            if not new_q.empty():
                yield from _walk_queue(new_q)

        q = Queue()
        q.put(node)
        yield from _walk_queue(q)

    def walk_stack(self, node):
        def _walk_stack(q):
            new_q = []
            while len(q) != 0:
                n = q.pop()
                yield n
                if n.left is not None:
                    new_q.append(n.left)
                if n.right is not None:
                    new_q.append(n.right)
            if len(new_q) != 0:
                yield from _walk_stack(new_q)

        q = []
        q.append(node)
        yield from _walk_stack(q)

    def search(self, key):
        def _search(current_node, key):
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node.key:
                return _search(current_node.left, key)
            else:
                return _search(current_node.right, key)

        return _search(self.root, key)

    def min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not None:
            return self.min(node.right)
        while node.parent is not None and node is node.parent.right:
            node = node.parent
        return node.parent

    def predecessor(self, node):
        if node.left is not None:
            return self.max(node.left)
        while node.parent is not None and node is node.parent.left:
            node = node.parent
        return node.parent

    def delete(self, node):
        if node.parent is None:
            self.root = None
            return
        
        if node.left is None:
            self._transplant(node.right, node)
        elif node.right is None:
            self._transplant(node.left, node)
        else:
            replacement = self.min(node.right)
            self._transplant(replacement.right, replacement)
            self._transplant(replacement, node)

    def _transplant(self, node, target):
        if target.parent is None:
            self.root = node
            return

        if target is target.parent.left:
            target.parent.left = node
        else:
            target.parent.right = node
        if node is not None:
            node.parent = target.parent
            
    def display(self):
        for i in self.walk_inorder(self.root):
            print(i.key, i.parent.key if i.parent is not None else 'None',
                    i.left.key if i.left is not None else 'None',
                    i.right.key if i.right is not None else 'None')
