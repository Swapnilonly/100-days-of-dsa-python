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


# 733. Flood Fill

**LeetCode:** [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
**Difficulty:** Easy
**Topic:** Graph, DFS, Matrix

---

## Problem

Given an `m × n` image, start from pixel `(sr, sc)` and change its color to the given `color`.

Change all pixels that:

* Have the **same original color** as the starting pixel.
* Are **directly connected** horizontally or vertically.

Diagonal cells are not considered connected.

---

## Example

```text
Input:

1 1 1
1 1 0
1 0 1

Start = (1,1)
New Color = 2
```

```text
Output:

2 2 2
2 2 0
2 0 1
```

The bottom-right `1` remains unchanged because it is not connected to the starting pixel.

---

## Approach

Use **DFS (Depth-First Search)** to visit all connected pixels having the original color.

### Steps

1. Store the starting pixel's original color.
2. If the original color is already equal to the new color, return the image.
3. Start DFS from `(sr, sc)`.
4. Check whether the current cell is inside the grid.
5. If its color is different from the original color, stop.
6. Change the current cell to the new color.
7. Recursively visit the four adjacent cells:

   * Up
   * Down
   * Left
   * Right
8. Return the modified image.

### Direction Diagram

```text
        Up
         ↑
         |
Left ← Current → Right
         |
         ↓
       Down
```

---

## Edge Case

If:

```text
image[sr][sc] == color
```

return immediately.

Otherwise, DFS can keep processing cells without actually changing their color.

---

## Complexity

**Time:** `O(m × n)`

**Space:** `O(m × n)` in the worst case due to recursion.

---

## Key Takeaway

Flood Fill is a **DFS/BFS grid traversal** problem.

Think of:

```text
Grid Cell = Node
Adjacent Cell = Edge
DFS/BFS = Traversal
Same Color = Condition
```

The same pattern is useful for problems like **Number of Islands** and **Max Area of Island**.

---

## Pattern

**Grid → 4 Directions → DFS/BFS → Connected Component**

---

## Word of the Day

**Adjacent** — directly next to something.

Example:
`Cells sharing a side are adjacent cells.`


# 🌴 Number of Islands

**LeetCode:** [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
**Difficulty:** Medium
**Topic:** Graph, DFS, BFS, Grid Traversal

---

## 📝 Problem

Given an `m x n` binary grid:

* `"1"` represents **land**
* `"0"` represents **water**

An island is formed by connecting adjacent land cells **horizontally or vertically**.

Return the **number of islands**.

Diagonal connections are **not allowed**.

### Example

```text
1 1 0 0
1 0 0 1
0 0 1 1
```

There are **2 islands**.

---

## 💡 Approach

Treat the grid as a **graph**:

* Each land cell (`"1"`) = node
* Adjacent land cells = connected nodes
* One connected group of land = one island

Use **DFS** to explore each complete island.

---

## 🔢 Steps

1. Traverse every cell of the grid.
2. If the cell is `"0"`, ignore it.
3. If the cell is `"1"` and not visited:

   * Increment the island count.
   * Start DFS from that cell.
4. In DFS, visit the cell and check its four directions:

   * Top
   * Bottom
   * Left
   * Right
5. Mark connected land cells as visited.
6. Continue scanning the grid.
7. Return the total island count.

### Direction Pattern

```text
       Top
        ↑
        |
Left ←  X  → Right
        |
        ↓
      Bottom
```

---

## 🔍 Key Idea

The important observation is:

> **Every time we find an unvisited land cell, we have discovered a new island.**

DFS then explores the entire connected island so that its other cells are not counted as separate islands.

```text
New "1"
   ↓
New Island → count + 1
   ↓
DFS
   ↓
Visit all connected "1"s
```

---

## ⚠️ Edge Cases

* Empty grid
* Grid containing only water
* Grid containing only land
* Single-cell island
* Diagonal land cells are separate islands

Example:

```text
1 0
0 1
```

Answer:

```text
2
```

because diagonal cells are not connected.

---

## ⏱️ Complexity

**Time:** `O(m × n)`

Each cell is processed at most once.

**Space:** `O(m × n)`

For the `visited` set and DFS recursion stack in the worst case.

---

## 🔗 Pattern

**Connected Components + DFS/BFS**

This problem is essentially finding the number of **connected components** in a grid.

Similar problems:

* Flood Fill
* Number of Provinces
* Max Area of Island
* Surrounded Regions

---

## 🎯 Key Takeaway

> **Scan the entire grid → find an unvisited ****`1`**** → count one island → DFS/BFS to visit the complete connected component.**

The main difference from **Flood Fill** is that Flood Fill explores one given component, while Number of Islands requires us to **find and count every connected component**.


# 🏝️ Max Area of Island

**LeetCode:** [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
**Difficulty:** Medium
**Topic:** Graph, DFS, Matrix, Connected Components

---

## 📝 Problem

Given a binary matrix `grid`, where:

* `1` represents **land**
* `0` represents **water**

Find the **maximum area of an island**.

An island is a group of connected `1`s connected **up, down, left, or right**.

---

## 💡 Approach

Use **DFS (Depth-First Search)** to explore every island.

For each unvisited land cell:

1. Start DFS.
2. Mark the cell as visited.
3. Count the current cell as `1`.
4. Explore its four neighboring cells.
5. Add the areas returned by those recursive calls.
6. Return the total area of that island.
7. Update `max_area`.

---

## 🔢 Steps

1. Create a `visited` set to track visited cells.
2. Traverse every cell in the grid.
3. If the cell is land (`1`) and not visited:

   * Start DFS.
   * Calculate the complete island area.
4. Compare the island area with `max_area`.
5. Return `max_area`.

### DFS Directions

```text
        Up
        ↑
Left ← Cell → Right
        ↓
       Down
```

---

## ⚠️ Edge Cases

* Grid contains only water → `0`
* Grid contains one island → return its area
* Multiple separate islands → return the largest area
* Single-cell island → area is `1`
* Island touches the boundary → still count normally

---

## ⏱️ Complexity

**Time:** `O(rows × cols)`

Each cell is visited at most once.

**Space:** `O(rows × cols)`

For the `visited` set and recursion stack.

---

## 🔑 Key Takeaway

The important idea is:

> **DFS can return the size of a connected component.**

For every land cell:

```text
Island Area =
Current Cell
+ Top
+ Bottom
+ Left
+ Right
```

This makes the problem a **Connected Components** problem on a grid.

---

## 🧩 Pattern

**Grid + Connected Cells + Largest/Smallest Component**

→ Think **DFS/BFS + Visited**

Common problems using the same pattern:

* Number of Islands
* Max Area of Island
* Flood Fill
* Number of Provinces
* Connected Components

##
