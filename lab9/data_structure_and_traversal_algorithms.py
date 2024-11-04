# Step 1: Implement the Graph Class

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()




# Step 2: Implement Depth-First Search (DFS)

class Graph:
    def __init__(self):
        """Initialize an empty graph as a dictionary."""
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def dfs(self, start_vertex):
        """Perform DFS starting from the given vertex."""
        visited = set()  # Set to keep track of visited vertices
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        """Recursive helper function for DFS."""
        visited.add(vertex)
        print(vertex, end=' ')  # Print the current vertex
        
        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Test DFS
print("DFS starting from vertex 0:")
g.dfs(0)






# Step 3: Implement Breadth-First Search (BFS)

from collections import deque

class Graph:
    def __init__(self):
        """Initialize an empty graph as a dictionary."""
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def bfs(self, start_vertex):
        """Perform BFS starting from the given vertex."""
        visited = set()  # Set to keep track of visited vertices
        queue = deque([start_vertex])  # Initialize the queue with the starting vertex
        visited.add(start_vertex)  # Mark the starting vertex as visited

        while queue:
            vertex = queue.popleft()  # Dequeue a vertex
            print(vertex, end=' ')  # Print the current vertex

            # Enqueue all unvisited neighbors
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    queue.append(neighbor)  # Add to queue

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Test BFS
print("BFS starting from vertex 0:")
g.bfs(0)






# Step 4: Implement a Method to Find All Paths

class Graph:
    def __init__(self):
        """Initialize an empty graph as a dictionary."""
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def find_all_paths(self, start_vertex, end_vertex, path=None):
        """Find all paths from start_vertex to end_vertex."""
        if path is None:
            path = []  # Initialize path on first call
        path = path + [start_vertex]  # Add current vertex to path

        if start_vertex == end_vertex:  # If the current vertex is the end vertex
            return [path]  # Return the current path

        if start_vertex not in self.graph:  # If the start vertex is not in the graph
            return []  # No paths to return

        paths = []  # List to store all paths
        for neighbor in self.graph[start_vertex]:  # Explore neighbors
            if neighbor not in path:  # Avoid revisiting vertices
                new_paths = self.find_all_paths(neighbor, end_vertex, path)  # Recursive call
                for new_path in new_paths:  # Collect all new paths
                    paths.append(new_path)
        return paths  # Return all found paths

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Test finding all paths
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))




# Step 5: Implement a Method to Check if the Graph is Connected

class Graph:
    def __init__(self):
        """Initialize an empty graph as a dictionary."""
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []  # Initialize the vertex with an empty list

    def _dfs_recursive(self, vertex, visited):
        """Helper function for depth-first search."""
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def is_connected(self):
        """Check if the graph is connected."""
        if not self.graph:
            return True  # An empty graph is considered connected
        start_vertex = next(iter(self.graph))  # Get an arbitrary starting vertex
        visited = set()
        self._dfs_recursive(start_vertex, visited)  # Perform DFS from the starting vertex
        return len(visited) == len(self.graph)  # Check if all vertices were visited

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)  # This vertex is already in the graph but is not connected
g.add_vertex(5)  # Adding a new disconnected vertex
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())






# Exercises


# 1.Find the Shortest Path Between Two Vertices Using BFS

def shortest_path(self, start_vertex, end_vertex):
    """Find the shortest path between two vertices using BFS."""
    visited = set()
    queue = deque([[start_vertex]])  # Initialize queue with the start vertex in a path

    while queue:
        path = queue.popleft()
        vertex = path[-1]  # Get the last vertex in the current path

        if vertex == end_vertex:
            return path  # Return the path if we reached the end vertex
        
        if vertex not in visited:
            visited.add(vertex)  # Mark the vertex as visited

            for neighbor in self.graph[vertex]:
                new_path = list(path)  # Create a new path
                new_path.append(neighbor)  # Append the neighbor to the path
                queue.append(new_path)  # Add new path to the queue
    return None  # Return None if no path exists

# Add to Graph class and test
Graph.shortest_path = shortest_path

# Test the shortest path method
print("\nShortest path from vertex 0 to vertex 3:")
shortest = g.shortest_path(0, 3)
print(' -> '.join(map(str, shortest))) if shortest else print("No path found")




# 2.Detect Cycles in the Graph

def has_cycle(self):
    """Detect cycles in the graph using DFS."""
    visited = set()

    def _has_cycle_recursive(vertex, parent):
        visited.add(vertex)  # Mark the vertex as visited
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if _has_cycle_recursive(neighbor, vertex):  # Recur for DFS
                    return True
            elif parent != neighbor:  # Check for back edges
                return True
        return False

    for vertex in self.graph:
        if vertex not in visited:
            if _has_cycle_recursive(vertex, None):
                return True  # Cycle detected
    return False  # No cycles detected

# Add to Graph class and test
Graph.has_cycle = has_cycle

# Test for cycles
print("\nDoes the graph have a cycle?", g.has_cycle())





# 3.Implement Dijkstra's Algorithm

import heapq

def dijkstra(self, start_vertex):
    """Find the shortest paths from start_vertex to all other vertices using Dijkstra's algorithm."""
    # Create a priority queue
    queue = []
    heapq.heappush(queue, (0, start_vertex))  # (distance, vertex)
    distances = {vertex: float('inf') for vertex in self.graph}  # Initialize distances
    distances[start_vertex] = 0  # Distance to start vertex is 0
    previous_vertices = {vertex: None for vertex in self.graph}  # Track previous vertices

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)  # Get vertex with the smallest distance

        for neighbor in self.graph[current_vertex]:
            distance = current_distance + 1  # Assuming all edges have a weight of 1
            if distance < distances[neighbor]:  # Relaxation
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_vertices  # Return the distances and the path information

# Add to Graph class and test
Graph.dijkstra = dijkstra

# Test Dijkstra's algorithm (Note: graph should be initialized with weights)
print("\nShortest paths from vertex 0:")
distances, previous = g.dijkstra(0)
print(distances)





# 4.Check if the Graph is Bipartite

def is_bipartite(self):
    """Check if the graph is bipartite."""
    color = {}
    
    def bfs(start_vertex):
        queue = deque([start_vertex])
        color[start_vertex] = 0  # Color the start vertex with color 0

        while queue:
            vertex = queue.popleft()
            for neighbor in self.graph[vertex]:
                if neighbor not in color:  # If the neighbor hasn't been colored
                    color[neighbor] = 1 - color[vertex]  # Assign alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[vertex]:  # If same color as parent
                    return False  # Not bipartite
        return True

    for vertex in self.graph:
        if vertex not in color:  # If the vertex hasn't been colored
            if not bfs(vertex):  # Check using BFS
                return False  # Not bipartite

    return True  # All vertices colored successfully

# Add to Graph class and test
Graph.is_bipartite = is_bipartite

# Test bipartite check
print("\nIs the graph bipartite?", g.is_bipartite())












# Step 1: Implement Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)



# Step 2: Implement Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)




# Step 3: Implement Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)





# Step 4: Compare Performance

import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)





# Exercises 

# 1.Implement an in-place version of Quick Sort

def quick_sort_in_place(arr, low=0, high=None):
    """In-place Quick Sort implementation."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """Helper function for in-place Quick Sort to partition the array."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test in-place Quick Sort
in_place_test_arr = test_arr.copy()
quick_sort_in_place(in_place_test_arr)
print("In-place Quick Sort Result:", in_place_test_arr)





# 2.Modify Bubble Sort to stop early if the list becomes sorted

def optimized_bubble_sort(arr):
    """Optimized Bubble Sort that stops early if the array is sorted."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps were made, the list is already sorted
            break
    return arr

# Test optimized Bubble Sort
print("Optimized Bubble Sort Result:", optimized_bubble_sort(test_arr.copy()))





# 3.Hybrid Sort (Merge Sort + Insertion Sort for small subarrays)

def insertion_sort(arr):
    """Helper function to perform Insertion Sort on a small array."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def hybrid_merge_sort(arr, threshold=10):
    """Hybrid Merge Sort that uses Insertion Sort for small subarrays."""
    if len(arr) <= threshold:
        return insertion_sort(arr)
    
    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)
    
    return merge(left, right)

# Test hybrid Merge Sort
print("Hybrid Merge Sort Result:", hybrid_merge_sort(test_arr.copy()))





# 4.Visualization of Sorting Algorithms using Matplotlib

import matplotlib.pyplot as plt
import time

def visualize_sorting_algorithm(algorithm, arr):
    """Function to visualize the sorting algorithm."""
    fig, ax = plt.subplots()
    ax.set_title(f"Visualizing {algorithm.__name__}")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge", color="skyblue")

    def update(arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        plt.pause(0.05)  # Pause for a moment to see the sorting progress

    # Copy the array and sort it using the provided algorithm
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    # Using Bubble Sort algorithm for visualization
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
                update(arr_copy, bar_rects)
        if not swapped:
            break

    plt.show()

# Test visualization
test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_sorting_algorithm(bubble_sort, test_arr.copy())