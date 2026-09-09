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




# 🌳 Subtree of Another Tree

**LeetCode:** [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

---

## 📌 Problem

Given the roots of two binary trees `root` and `subRoot`, determine whether `subRoot` is a subtree of `root`.

A subtree must have the **same structure and node values** as a portion of the main tree.

### Example

```text
root:

        3
       / \
      4   5
     / \
    1   2


subRoot:

      4
     / \
    1   2
```

Output:

```text
True
```

The tree rooted at `4` is exactly the same as `subRoot`.

---

## 💡 Approach

Use **Recursion + Tree Comparison**.

The problem can be divided into two tasks:

1. **Search** for a node in `root` that could be the root of `subRoot`.
2. **Compare** both trees to check whether they are exactly identical.

We use a helper function `isSameTree()` to compare two trees.

### Algorithm

```text
                 root
                   |
          Is root == subRoot?
             /           \
           Yes             No
            |               |
      Compare trees     Search left
                        and right
```

---

## 🔄 Steps

1. If `subRoot` is `None`, return `True`.
2. If `root` is `None`, return `False`.
3. Check whether the trees rooted at `root` and `subRoot` are identical.
4. If they are identical, return `True`.
5. Otherwise, recursively search in:

   * `root.left`
   * `root.right`
6. Return `True` if either side contains `subRoot`.

### Tree Comparison

For `isSameTree()`:

1. If both nodes are `None`, return `True`.
2. If only one node is `None`, return `False`.
3. If their values are different, return `False`.
4. Recursively compare:

   * Left subtrees
   * Right subtrees
5. Both sides must match.

---

## 🧠 Key Idea

```text
isSubtree()
     |
     ├── Find possible matching node
     |
     └── isSameTree()
              |
              ├── Compare values
              ├── Compare left subtree
              └── Compare right subtree
```

The important distinction is:

* `isSubtree()` → **searches**
* `isSameTree()` → **compares**

---

## ⏱️ Complexity

Let:

* `n` = number of nodes in `root`
* `m` = number of nodes in `subRoot`

### Time Complexity

```text
O(n × m)
```

In the worst case, we may compare `subRoot` with many nodes of `root`.

### Space Complexity

```text
O(h)
```

where `h` is the height of the tree, due to recursion.

For a skewed tree:

```text
O(n)
```

---

## 🔑 Pattern Learned

**Tree Traversal + Tree Comparison**

This pattern is useful for problems where we need to:

* Find a tree inside another tree
* Compare two binary trees
* Check whether two subtrees are identical
* Search for a particular tree structure



# Validate Binary Search Tree

[LeetCode 98 — Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

## 📌 Problem

Given the root of a binary tree, determine whether it is a valid **Binary Search Tree (BST)**.

A valid BST follows these rules:

* All nodes in the left subtree must have values **less than** the current node.
* All nodes in the right subtree must have values **greater than** the current node.
* The same rule must be true for **every node** in the tree.

---

## 💡 Approach

### Algorithm: **DFS with Range Validation**

Instead of checking only the immediate children of each node, maintain a valid range `(min, max)` for every node.

For each node:

1. Check whether its value lies within the allowed range.
2. For the left subtree:

   * Update the upper bound to the current node's value.
3. For the right subtree:

   * Update the lower bound to the current node's value.
4. If any node violates its range, return `False`.
5. If all nodes satisfy their ranges, return `True`.

### Example

```text
        5
       / \
      3   8
     / \   \
    2   4   9
```

Start with:

```text
5 → (-∞, +∞)
```

Then:

```text
3 → (-∞, 5)
8 → (5, +∞)

2 → (-∞, 3)
4 → (3, 5)
9 → (8, +∞)
```

Every node stays within its valid range → **Valid BST**.

---

## 🔄 Algorithm Steps

1. Start DFS from the root with range `(-∞, +∞)`.
2. If the node is `None`, return `True`.
3. If `node.val` is not within `(min, max)`, return `False`.
4. Recursively validate the left subtree with:

   ```text
   (min, node.val)
   ```
5. Recursively validate the right subtree with:

   ```text
   (node.val, max)
   ```
6. Return `True` only if both subtrees are valid.

---

## ⏱️ Complexity

* **Time:** `O(n)` — every node is visited once.
* **Space:** `O(h)` — recursion stack, where `h` is the height of the tree.

  * Balanced tree: `O(log n)`
  * Skewed tree: `O(n)`

---

## ⚠️ Important Insight

Checking only the immediate children is **not enough**.

```text
        5
       / \
      3   7
       \
        6   ❌
```

`6 > 3`, so it looks valid when checking node `3`.

But `6` is inside the **left subtree of `5`**, so it must be `< 5`.

Therefore, the tree is invalid.

The key idea is to maintain the **valid range inherited from all ancestors**.

---


# Kth Smallest Element in a BST

## 💡 Intuition

In a **Binary Search Tree (BST)**, **inorder traversal** visits nodes in sorted order:

```text
Left → Root → Right
```

Therefore, if we count nodes during inorder traversal, the node where `count == k` is the **kth smallest element**.

---

## 🚀 Approach

1. Recursively visit the **left subtree** first.
2. Increment `count` when visiting the current node.
3. If `count == k`, store the current node's value in `ans`.
4. Only visit the **right subtree** if `count < k`, avoiding unnecessary traversal after finding the answer.
5. Return `ans`.

---

## 🧠 Algorithm

**Inorder Traversal**

```text
1. Traverse left subtree
2. Process current node
   → count += 1
3. If count == k
   → store current node value
4. Traverse right subtree
```

Because a BST produces values in ascending order during inorder traversal, the `k`th visited node is the kth smallest element.

---

## ⏱️ Complexity

### Time Complexity

**O(h + k)** in the optimized traversal, where:

* `h` = height of the tree
* `k` = position of the required element

Worst case: **O(n)**

### Space Complexity

**O(h)** for the recursion stack.

Where `h` is the height of the tree.

---

## 📌 Key Concept

> **Inorder traversal of a BST produces elements in sorted order.**

This makes inorder traversal the natural approach for finding the **kth smallest element** in a BST.



# Construct Binary Tree from Preorder and Inorder Traversal

**LeetCode:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## 📌 Problem

Given two integer arrays:

* `preorder` — represents the preorder traversal of a binary tree.
* `inorder` — represents the inorder traversal of the same binary tree.

Construct and return the original binary tree.

### Traversals

**Preorder:**

```text
Root → Left → Right
```

**Inorder:**

```text
Left → Root → Right
```

### Example

```text
Preorder = [3, 9, 20, 15, 7]
Inorder  = [9, 3, 15, 20, 7]
```

Constructed tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

---

## 💡 Approach

### Algorithm: Recursion + Hash Map

The key observation is:

* The **first element of preorder** is always the root.
* Find this root in `inorder`.
* Elements to the **left** of the root belong to the left subtree.
* Elements to the **right** of the root belong to the right subtree.
* Recursively construct both subtrees.

A hash map is used to store the index of every value in `inorder`, allowing the root position to be found in `O(1)` average time.

---

## 🚀 Steps

1. Create a hash map containing each `inorder` value and its index.
2. Maintain a pointer to the current element in `preorder`.
3. For the current recursive range:

   * If `start > end`, return `None`.
   * Take the current preorder element as the root.
   * Move the preorder pointer forward.
4. Find the root's index in `inorder`.
5. Recursively construct the **left subtree** using:

   ```text
   start → root_index - 1
   ```
6. Recursively construct the **right subtree** using:

   ```text
   root_index + 1 → end
   ```
7. Return the root node.

---

## 🔍 How the Tree Gets Connected

Each recursive call returns the root of its subtree.

```text
root.left  = left_subtree
root.right = right_subtree
```

For example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The recursive calls effectively create:

```text
3.left  = 9
3.right = 20

20.left  = 15
20.right = 7
```

So recursion doesn't just create nodes — the returned subtree roots are assigned to the parent's `left` and `right` pointers.

---

## 🧠 Key Insight

> **Preorder tells us WHO is the root, while inorder tells us WHERE to split the left and right subtrees.**

For:

```text
Preorder = [3, 9, 20, 15, 7]
Inorder  = [9, 3, 15, 20, 7]
```

First preorder element:

```text
3
```

is the root.

In inorder:

```text
[9, 3, 15, 20, 7]
    ↑
```

Therefore:

```text
Left subtree  → [9]
Right subtree → [15, 20, 7]
```

The same process is repeated recursively for each subtree.

---

## ⏱️ Complexity

### Time Complexity

```text
O(n)
```

Each node is processed once, and the hash map provides `O(1)` average lookup for the root's position.

### Space Complexity

```text
O(n)
```

* `O(n)` for the inorder hash map.
* `O(n)` worst-case recursion stack for a skewed tree.

---

## 🔑 Important Concepts

* Binary Tree
* Preorder Traversal
* Inorder Traversal
* Recursion
* Hash Map
* Divide and Conquer
* Recursive Tree Construction
* Tree Node Linking
