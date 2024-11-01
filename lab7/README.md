# Binary Search Tree (BST) Implementation in Python

This repository contains a Python implementation of a Binary Search Tree (BST) with various operations such as insertion, deletion, searching, and different types of traversals. The implementation also includes features to find the maximum value, count the total number of nodes, perform level-order traversal, check the height of the tree, and validate if the tree is a valid BST.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Overview

The `BinarySearchTree` class represents a binary search tree, with the `Node` class representing each node in the tree. Each node contains a value, and references to its left and right children.

## Features

The `BinarySearchTree` class provides the following methods:

1. **insert(value)**: Inserts a new value into the BST.
2. **search(value)**: Searches for a value in the BST.
3. **inorder_traversal()**: Returns the values in in-order (sorted) order.
4. **preorder_traversal()**: Returns the values in pre-order.
5. **postorder_traversal()**: Returns the values in post-order.
6. **delete(value)**: Deletes a specified value from the BST.
7. **max_value()**: Returns the maximum value in the BST.
8. **count_nodes()**: Returns the total number of nodes in the BST.
9. **level_order_traversal()**: Returns the values in level-order (breadth-first).
10. **height()**: Returns the height of the BST.
11. **is_valid_bst()**: Checks if the tree is a valid binary search tree.

## Getting Started

To use this Binary Search Tree implementation:

1. Clone or download the repository.
2. Open the Python file and run the script.

## Usage

Here’s how to use the `BinarySearchTree` class:

```python
# Create a Binary Search Tree
bst = BinarySearchTree()

# Insert values into the BST
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Search for a value
print(bst.search(4))  # Should return a Node with value 4
print(bst.search(9))  # Should return None

# Traversals
print("In-order:", bst.inorder_traversal())  # Output: [2, 3, 4, 5, 6, 7, 8]
print("Pre-order:", bst.preorder_traversal())  # Output: [5, 3, 2, 4, 7, 6, 8]
print("Post-order:", bst.postorder_traversal())  # Output: [2, 4, 3, 6, 8, 7, 5]

# Delete a value
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())  # Output: [2, 4, 5, 6, 7, 8]

# Additional operations
print("Maximum value:", bst.max_value())  # Output: 8
print("Total nodes:", bst.count_nodes())  # Output: 6
print("Level-order traversal:", bst.level_order_traversal())  # Output: [5, 2, 7, 4, 6, 8]
print("Height of tree:", bst.height())  # Output: 2
print("Is valid BST:", bst.is_valid_bst())  # Output: True
