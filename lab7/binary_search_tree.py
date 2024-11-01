class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

# Testing the class
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Testing search
print(bst.search(4))  # Should return a Node with value 4
print(bst.search(9))  # Should return None

# Testing traversals
print("In-order:", bst.inorder_traversal())
print("Pre-order:", bst.preorder_traversal())
print("Post-order:", bst.postorder_traversal())

# Testing delete
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    # 1. Find the maximum value in the BST
    def max_value(self):
        current = self.root
        while current.right:
            current = current.right
        return current.value if current else None

    # 2. Count the total number of nodes in the BST
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    # 3. Level-order traversal (breadth-first search)
    def level_order_traversal(self):
        result = []
        if not self.root:
            return result
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    # 4. Find the height of the BST
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # height of an empty tree is -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    # 5. Check if the tree is a valid BST
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_value, max_value):
        if node is None:
            return True
        if not (min_value < node.value < max_value):
            return False
        return (self._is_valid_bst_recursive(node.left, min_value, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_value))

# Testing the class
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Testing max_value
print("Maximum value:", bst.max_value())

# Testing count_nodes
print("Total nodes:", bst.count_nodes())

# Testing level_order_traversal
print("Level-order traversal:", bst.level_order_traversal())

# Testing height
print("Height of tree:", bst.height())

# Testing is_valid_bst
print("Is valid BST:", bst.is_valid_bst())

# Testing delete
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())
