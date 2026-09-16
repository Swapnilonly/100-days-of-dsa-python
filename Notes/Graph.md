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
