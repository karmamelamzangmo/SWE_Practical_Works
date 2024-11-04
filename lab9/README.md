# Graph and Sorting Algorithms in Python

This project implements various algorithms for working with graphs and sorting data. The code includes implementations for creating graphs, performing depth-first and breadth-first searches, finding paths, checking graph connectivity, and various sorting algorithms. Additionally, it provides methods for visualizing sorting algorithms using `matplotlib`.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Graph Operations](#graph-operations)
- [Sorting Algorithms](#sorting-algorithms)
- [Visualizing Sorting](#visualizing-sorting)
- [Examples](#examples)

## Features
### Graph Algorithms
- **Graph Creation**: Add vertices and edges to form an undirected graph.
- **DFS and BFS Traversals**: Depth-First Search and Breadth-First Search to explore nodes.
- **Finding All Paths**: Recursive search for all paths between two vertices.
- **Connectivity Check**: Check if the graph is fully connected.
- **Shortest Path (BFS)**: Find the shortest path between two vertices.
- **Cycle Detection**: Detect cycles using DFS.
- **Dijkstra's Algorithm**: Find shortest paths in a weighted graph.
- **Bipartite Check**: Determine if the graph is bipartite.

### Sorting Algorithms
- **Bubble Sort**: Standard bubble sort with early stopping if already sorted.
- **Merge Sort**: Recursive merge sort.
- **Quick Sort**: Recursive quick sort.
- **In-Place Quick Sort**: Quick sort without extra space.
- **Hybrid Merge Sort**: Merge sort that switches to insertion sort for small subarrays.

### Sorting Visualization
- Visualize sorting steps with `matplotlib`, observing how sorting algorithms rearrange elements.

## Getting Started
1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/graph-sorting-algorithms.git
    cd graph-sorting-algorithms
    ```

2. **Install Dependencies**
    This project requires `matplotlib` for visualization.
    ```bash
    pip install matplotlib
    ```

3. **Run the Code**
    Each class and function can be tested individually by running the examples in this README or adding your own test cases.

## Graph Operations
The `Graph` class is the main structure for graph-related methods.

```python
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.dfs(0)  # Depth-First Search from vertex 0
g.bfs(0)  # Breadth-First Search from vertex 0
paths = g.find_all_paths(0, 3)  # Find all paths from 0 to 3
print("All paths from 0 to 3:", paths)
