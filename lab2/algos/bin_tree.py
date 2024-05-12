class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = Node(key, data)
        else:
            self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, data)
            else:
                self._insert(node.left, key, data)
        else:
            if node.right is None:
                node.right = Node(key, data)
            else:
                self._insert(node.right, key, data)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return []
        elif key == node.key:
            return (
                [node.data]
                + self._search(node.left, key)
                + self._search(node.right, key)
            )
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
