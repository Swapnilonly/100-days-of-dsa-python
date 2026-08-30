📌 Problem

Given the root of a binary tree, invert the tree and return its root.

Inverting a binary tree means swapping the left and right children of every node.

Example
Input:

       4
      / \
     2   7
    / \ / \
   1  3 6  9


Output:

       4
      / \
     7   2
    / \ / \
   9  6 3  1
💡 Approach
Recursive DFS

The same operation needs to be performed on every node:

Swap left and right
        ↓
Invert left subtree
        ↓
Invert right subtree
Algorithm
If root is None, return None.
Swap the left and right children of the current node.
Recursively invert the left subtree.
Recursively invert the right subtree.
Return the root.



# 102. Binary Tree Level Order Traversal

**LeetCode:** [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
**Difficulty:** Medium
**Topic:** Binary Tree, BFS, Queue

---

## 📌 Problem

Given the root of a binary tree, return the **level order traversal** of its nodes' values.

The nodes should be traversed:

* From **left to right**
* **Level by level**

### Example

```text
        3
       / \
      9   20
         /  \
        15   7
```

**Input:**

```text
[3,9,20,null,null,15,7]
```

**Output:**

```text
[[3], [9,20], [15,7]]
```

---

## 💡 Approach

Use **BFS (Breadth-First Search)** with a **Queue**.

A queue follows **FIFO (First In, First Out)**, which makes it suitable for processing nodes level by level.

### Why Queue?

```text
        3
       / \
      9   20
         /  \
        15   7

Queue:
[3]
 ↓
[9, 20]
 ↓
[15, 7]
```

The queue ensures that nodes are processed in the same order in which they are discovered.

---

## 🔹 Algorithm

1. If `root` is `None`, return an empty list.
2. Create a queue and insert the `root`.
3. While the queue is not empty:

   * Store the number of nodes currently in the queue using `level_size`.
   * Create an empty `current_level` list.
   * Process exactly `level_size` nodes.
   * Remove each node from the front of the queue.
   * Add its value to `current_level`.
   * Add its left child to the queue if it exists.
   * Add its right child to the queue if it exists.
4. Add `current_level` to `res`.
5. Return `res`.

---

## ⚠️ Important Concept: `level_size`

This is the key part of the solution:

```python
level_size = len(queue)
```

It tells us **how many nodes belong to the current level**.

For example:

```text
queue = [9, 20]

level_size = 2
```

Even after processing `9` and adding its children, we still process only the original `2` nodes of that level.

```text
Current Level
     ↓
[9, 20]
     ↓
Process exactly 2 nodes
     ↓
Children → next level
```

This is what allows us to keep different levels separate.

---

## ⏱️ Complexity

### Time Complexity

```text
O(N)
```

Every node is visited exactly once.

### Space Complexity

```text
O(N)
```

The queue can contain up to `N` nodes in the worst case.

---

## 🧠 Pattern

```text
Tree
 ↓
Need level-by-level traversal
 ↓
BFS
 ↓
Queue
 ↓
level_size = len(queue)
 ↓
Process current level
 ↓
Add children to queue
```

**Pattern to remember:**

> **Level Order Traversal = BFS + Queue + Level Size**

---

## 🔑 Key Takeaway

When a binary tree problem asks for:

* Level by level
* Left to right at each level
* Nearest nodes first

Think:

```text
BFS → Queue
```

And when the output needs **separate lists for each level**, use:

```python
level_size = len(queue)
```

to identify the nodes belonging to the current level.

---

## 📚 Related Concepts

* Binary Tree
* Breadth-First Search (BFS)
* Queue
* FIFO
* Level Order Traversal
* Tree Traversal

---

## 📝 Word of the Day

### **Traverse**

**Meaning:** To systematically visit or move through every part of a structure.

**Example:**

> We traverse the binary tree level by level using BFS.
