# LinkedList Python Implementation

This repository contains a Python implementation of a singly linked list with various common operations such as insertion, deletion, searching, and traversal. Additional features include cycle detection, merging two sorted lists, removing duplicates, finding the middle element, and reversing the list.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Overview

The `LinkedList` class implements a singly linked list in Python with the `Node` class representing each individual element (node) in the list. Each node contains data and a reference to the next node in the list.

## Features

The `LinkedList` class provides the following methods:

1. **append(data)**: Adds a new node with `data` to the end of the list.
2. **display()**: Displays the linked list elements.
3. **insert(data, position)**: Inserts a new node with `data` at the specified position.
4. **delete(data)**: Removes the first node that contains the specified `data`.
5. **search(data)**: Searches for a node with `data` and returns its position.
6. **reverse()**: Reverses the linked list.
7. **find_middle()**: Finds and returns the middle element of the list.
8. **has_cycle()**: Checks if the list contains a cycle.
9. **remove_duplicates()**: Removes duplicate elements from the linked list.
10. **merge_sorted(other)**: Merges the list with another sorted linked list and returns the result.

## Getting Started

To use this linked list implementation:

1. Clone or download the repository.
2. Open the Python file and run the script.

## Usage

Here’s how to use the `LinkedList` class:

```python
# Initialize the linked list and append elements
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Display the list
ll.display()  # Output: 1 -> 2 -> 3

# Insert an element at position 1
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3

# Delete an element with data = 2
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3

# Search for an element
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1

# Reverse the linked list
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1

# Find the middle element
print("Middle element:", ll.find_middle())  # Output: Middle element: 4

# Check if the list has a cycle
print("Has cycle:", ll.has_cycle())  # Output: False

# Remove duplicate elements
ll.append(2)
ll.append(3)
ll.remove_duplicates()
ll.display()  # Output: 1 -> 4 -> 3

# Merge with another sorted linked list
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_ll = ll1.merge_sorted(ll2)
merged_ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
