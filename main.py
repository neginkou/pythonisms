import time

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node:
            yield from self._in_order_traversal(node.left)
            yield node.value
            yield from self._in_order_traversal(node.right)

    def __str__(self):
        return str(self.to_list())

    def to_list(self):
        return list(self)

    def __repr__(self):
        return f"BinaryTree(Node({self.root.value}))" if self.root else "BinaryTree()"

    def __eq__(self, other):
        return self.to_list() == other.to_list()

    def __bool__(self):
        return self.root is not None

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper


