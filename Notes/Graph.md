# 1971. Find if Path Exists in Graph

* **LeetCode:** [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)
* **Difficulty:** Easy
* **Topic:** Graph, BFS, Adjacency List

## Problem

Given an undirected graph with `n` vertices and a list of edges, determine whether a valid path exists from `source` to `destination`.

Return `True` if a path exists; otherwise, return `False`.

## Example

```python
n = 6
edges = [[0,1], [0,2], [1,3], [2,4], [4,5]]
source = 0
destination = 5
```

**Output:**

```python
True
```

## Approach

Use **Breadth-First Search (BFS)** with an adjacency list to explore the graph from the source vertex.

### Steps

1. Create an adjacency list for all `n` vertices.
2. For each undirected edge `[u, v]`, add `v` to `u`'s neighbors and `u` to `v`'s neighbors.
3. Initialize a queue with the source vertex and a visited set containing the source.
4. While the queue is not empty, remove the front vertex.
5. If the current vertex is the destination, return `True`.
6. Add all unvisited neighbors to the queue and mark them as visited.
7. If the destination is never reached, return `False`.

## Complexity

* **Time Complexity:** O(V + E)
* **Space Complexity:** O(V + E)

Where `V` is the number of vertices and `E` is the number of edges.

## Key Takeaway

BFS explores all reachable vertices from the source. If the destination belongs to the same connected component, a valid path exists.

## Pattern

Graph Traversal + Adjacency List + BFS + Visited Set

## Word of the Day

**Reachability:** The ability to get from one vertex to another through graph connections.



# 547. Number of Provinces

* **LeetCode:** [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
* **Difficulty:** Medium
* **Topic:** Graph, DFS, Adjacency Matrix, Connected Components

## Problem

Given an `n x n` adjacency matrix `isConnected`, where `isConnected[i][j] = 1` indicates a direct connection between city `i` and city `j`, return the total number of provinces.

A province is a group of directly or indirectly connected cities.

## Example

```python
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
```

**Output:**

```python
2
```

## Approach

Use Depth First Search (DFS) to count connected components in the graph.

### Steps

1. Create a `visited` array of size `n`, initialized to `False`.
2. Iterate through every city from `0` to `n - 1`.
3. If the city is unvisited, increment the province count.
4. Run DFS from that city to visit all directly and indirectly connected cities.
5. Mark each visited city to avoid revisiting it.
6. Return the total province count.

## Complexity

* **Time Complexity:** O(n²)
* **Space Complexity:** O(n)

## Key Takeaway

Each DFS started from an unvisited city represents one connected component, which corresponds to one province.

## Pattern

Graph Traversal + Connected Components + DFS + Adjacency Matrix

## Word of the Day

**Connectivity:** The property of being linked or connected within a graph.
