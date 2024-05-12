class Node:
    def __init__(
        self, key, data, color="red", left=None, right=None, parent=None
    ):
        self.key = key
        self.data = data
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, data=None, color="black")
        self.root = self.NIL

    def insert(self, key, data):
        new_node = Node(
            key,
            data,
            color="red",
            left=self.NIL,
            right=self.NIL,
            parent=self.NIL,
        )
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        else:
            if new_node.key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
        new_node.color = "red"
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = "black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, key):
        return self._search_tree(self.root, key)

    def _search_tree(self, node, key):
        if node == self.NIL:
            return []
        elif key == node.key:
            return (
                [node.data]
                + self._search_tree(node.left, key)
                + self._search_tree(node.right, key)
            )
        elif key < node.key:
            return self._search_tree(node.left, key)
        else:
            return self._search_tree(node.right, key)


# Пример использования
data_objects = [
    {"name": "apple", "value": 1},
    {"name": "banana", "value": 2},
    {"name": "apple", "value": 3},
]
rbt = RedBlackTree()
for obj in data_objects:
    rbt.insert(obj["name"], obj)

# Поиск всех объектов с ключом 'apple'
found_apples = rbt.search("apple")
print(found_apples)
