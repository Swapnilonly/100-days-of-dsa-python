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


# 🌳 Binary Tree Maximum Path Sum

**LeetCode:** https://leetcode.com/problems/binary-tree-maximum-path-sum/
**Difficulty:** Hard
**Topic:** Binary Tree, DFS, Recursion, Tree Dynamic Programming

---

## 📌 Problem

Given the root of a binary tree, find the **maximum path sum**.

A path can start and end at **any node** in the tree.

A path must follow connected nodes, but it **does not need to pass through the root**.

Each node can appear at most once in the path.

### Example

```text
        -10
        /  \
       9    20
           /  \
          15   7
```

The maximum path is:

```text
15 → 20 → 7
```

Sum:

```text
15 + 20 + 7 = 42
```

**Output:**

```text
42
```

---

## 💡 Approach

### Algorithm: Depth-First Search (DFS) + Recursion

For every node, calculate two things:

1. **Maximum path sum passing through the current node**
2. **Maximum one-sided path sum that can be returned to its parent**

The important idea is that a path passing through a node can use **both left and right subtrees**, but the value returned to the parent can use only **one side**.

---

## 🔍 Important Difference

This is the most important concept in the problem.

### Path through current node

```python
root.val + left + right
```

Can use:

```text
Left → Root → Right
```

Example:

```text
15 → 20 → 7

= 42
```

### Value returned to parent

```python
root.val + max(left, right)
```

Can use only:

```text
Root → Left
```

or:

```text
Root → Right
```

Example:

```text
20 → 15

= 35
```

---

## ⚠️ Edge Case: All Negative Nodes

Consider:

```text
       -3
       / \
     -5  -2
```

We **cannot** initialize:

```python
self.res = 0
```

because that would incorrectly return `0`.

Instead:

```python
self.res = float('-inf')
```

Now:

```text
-5 → res = -5
-2 → res = -2
-3 → res = -2
```

Correct answer:

```text
-2
```

The `max(..., 0)` is still used for subtree contributions because a negative subtree should simply be ignored.

---

## ⏱️ Complexity

### Time Complexity

```text
O(N)
```

Every node is visited exactly once.

### Space Complexity

```text
O(H)
```

where `H` is the height of the tree because of the recursion stack.

For a balanced tree:

```text
O(log N)
```

For a skewed tree:

```text
O(N)
```

---

## 🔑 Key Takeaway

The core idea is:

```python
# Maximum path passing through current node
root.val + left + right
```

but:

```python
# Maximum path that can be extended to parent
root.val + max(left, right)
```

Remember:

```text
                 Current Node
                /            \
               /              \
          left path        right path

        left + node + right
               ↓
          Global Answer

        node + max(left, right)
               ↓
          Return to Parent
```

Also remember:

```python
self.res = float('-inf')
```

because the answer can be negative.

##


# 🌳 Count Nodes With Average of Subtree

**LeetCode:** https://leetcode.com/problems/count-nodes-with-the-highest-average-subtree/
**Difficulty:** Easy
**Topic:** Binary Tree, DFS, Post-Order Traversal

---

## 📌 Problem

Given the root of a binary tree, count the number of nodes whose value is equal to the **average of all values in its subtree**.

The subtree includes:

* The current node
* All nodes in its left subtree
* All nodes in its right subtree

The average is calculated using integer division.

### Example

```text
        4
       / \
      8   5
     / \
    0   1
```

For node `0`:

```text
sum = 0
count = 1

average = 0 // 1
        = 0
```

```text
0 == 0 ✅
```

So node `0` is counted.

For node `8`:

```text
sum = 8 + 0 + 1
    = 9

count = 3

average = 9 // 3
        = 3
```

```text
3 != 8 ❌
```

For node `5`:

```text
sum = 5
count = 1

average = 5 // 1
        = 5
```

```text
5 == 5 ✅
```

Therefore, the nodes satisfying the condition are:

```text
0, 1, 5
```

**Output:**

```text
3
```

---

## 💡 Approach: Post-Order Traversal (DFS)

### Intuition

To compute the average of a subtree, we need the:

* **Sum** of all nodes in the subtree
* **Count** of all nodes in the subtree

A **bottom-up Post-Order Traversal** naturally gives us this information.

We first solve:

```text
Left Subtree
      ↓
Right Subtree
      ↓
Current Node
```

Then we combine the results at the current node.

The recursive function returns:

```python
(sum, count)
```

for every subtree.

---

## 🚀 Algorithm

1. Recursively traverse the **left child**.
2. Recursively traverse the **right child**.
3. Each recursive call returns:

   ```text
   [sum, count]
   ```

   of that subtree.
4. At the current node, calculate:

   ```text
   totalSum
   totalCount
   ```
5. Calculate the average:

   ```text
   totalSum // totalCount
   ```
6. If:

   ```text
   average == node.val
   ```

   increment the answer.
7. Return:

   ```text
   [totalSum, totalCount]
   ```

   to the parent.

---

## 🔄 Post-Order Traversal

Post-order means:

```text
Left → Right → Root
```

For this tree:

```text
        4
       / \
      8   5
     / \
    0   1
```

The traversal order is:

```text
0 → 1 → 8 → 5 → 4
```

This is useful because when we reach a node, we already know the information from both of its children.

---

## 🧠 Example Walkthrough

### Node `0`

```text
sum = 0
count = 1

average = 0 // 1
        = 0
```

```text
0 == 0 ✅
```

Return:

```text
(0, 1)
```

---

### Node `1`

```text
sum = 1
count = 1

average = 1 // 1
        = 1
```

```text
1 == 1 ✅
```

Return:

```text
(1, 1)
```

---

### Node `8`

Its children returned:

```text
left  = (0, 1)
right = (1, 1)
```

Now combine them with node `8`:

```text
totalSum = 0 + 1 + 8
         = 9

totalCount = 1 + 1 + 1
           = 3
```

Average:

```text
9 // 3 = 3
```

```text
3 != 8 ❌
```

Return:

```text
(9, 3)
```

---

### Node `5`

No children:

```text
totalSum = 5
totalCount = 1

average = 5 // 1
        = 5
```

```text
5 == 5 ✅
```

Return:

```text
(5, 1)
```

---

### Node `4`

Its children returned:

```text
left  = (9, 3)
right = (5, 1)
```

Combine:

```text
totalSum = 9 + 5 + 4
         = 18

totalCount = 3 + 1 + 1
           = 5
```

Average:

```text
18 // 5 = 3
```

```text
3 != 4 ❌
```

Final answer:

```text
3
```

---

## 💻 Solution

```python
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def func(node):
            if not node:
                return 0, 0

            lsum, lcount = func(node.left)
            rsum, rcount = func(node.right)

            summ = lsum + rsum + node.val
            count = lcount + rcount + 1

            if summ // count == node.val:
                self.res += 1

            return summ, count

        func(root)

        return self.res
```

---

## 🔑 Why Do We Return `(sum, count)`?

The parent needs information about the entire subtree of each child.

For example:

```text
        8
       / \
      0   1
```

After processing the children:

```text
0 → (0, 1)
1 → (1, 1)
```

Now node `8` can calculate:

```text
sum = 0 + 1 + 8
    = 9

count = 1 + 1 + 1
      = 3
```

So it returns:

```text
(9, 3)
```

Then its parent can use `(9, 3)` without traversing those nodes again.

This is the key **bottom-up** idea.

---

## 🎯 Pattern

### Post-Order DFS + Returning Multiple Values

Whenever a tree problem asks about information related to an entire subtree, think:

```text
         Current Node
        /            \
       ↓              ↓
 Left Subtree      Right Subtree
 (sum, count)      (sum, count)
       \              /
        \            /
         ↓          ↓
        Combine Results
               ↓
       Current Subtree
        (sum, count)
               ↓
        Return to Parent
```

This pattern can be useful for:

* Subtree Sum
* Subtree Size
* Subtree Average
* Counting nodes based on subtree properties
* Calculating minimum/maximum values in subtrees

---

## ⏱️ Complexity

### Time Complexity

```text
O(N)
```

Every node is visited exactly once.

### Space Complexity

```text
O(H)
```

where `H` is the height of the tree due to the recursion stack.

For a balanced tree:

```text
O(log N)
```

For a skewed tree:

```text
O(N)
```

---

## 🔑 Key Takeaway

The main idea is:

> **Solve the children first, then use their results to solve the current node.**

```text
Post-Order:

Left
 ↓
Right
 ↓
Root
```

Each DFS call returns:

```python
(sum, count)
```

Then:

```python
total_sum = left_sum + right_sum + node.val
total_count = left_count + right_count + 1
```

Finally:

```python
if total_sum // total_count == node.val:
    self.res += 1
```

So the core pattern is:

```text
Children's Information
        ↓
Combine
        ↓
Check Current Node
        ↓
Return Information to Parent
```

---

## 📝 Word of the Day

**Bottom-up** — solving smaller components first and using their results to solve the larger problem.

In this problem, we solve the **child subtrees first**, then calculate the result for the current node.



# 297. Serialize and Deserialize Binary Tree

**LeetCode:** https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

**Difficulty:** Hard

**Algorithm:** Preorder DFS + NULL Markers

---

## 📌 Problem

Design an algorithm to **serialize** a binary tree into a string and **deserialize** that string back into the original binary tree.

The reconstructed tree must have the **same structure and values** as the original tree.

---

## 💡 Approach

Use **Preorder Traversal**:

```text
Root → Left → Right
```

While serializing:

* Store each node's value.
* If a node is `None`, store `"null"`.
* Store the values in a list.
* Convert the list into a string using `",".join()`.

Example:

```text
        1
       / \
      2   3
         / \
        4   5
```

Serialized:

```text
1,2,null,null,3,4,null,null,5,null,null
```

The `null` markers are important because they preserve the **structure** of the tree.

---

## 🔄 Deserialization

Split the serialized string using `","` to get the values back.

Then reconstruct the tree using the same **Preorder order**:

```text
Root → Left → Right
```

### Steps

1. Read the current value.
2. If it is `"null"`, return `None`.
3. Otherwise, create a new `TreeNode`.
4. Recursively build its left subtree.
5. Recursively build its right subtree.
6. Return the created node.

---

## 🧠 Example

Serialized data:

```text
1,2,null,null,3,4,null,null,5,null,null
```

Reconstruction:

```text
        1
       / \
      2   3
         / \
        4   5
```

The first value is always the root in preorder.

For every node, the following values describe its:

```text
Left Subtree → Right Subtree
```

`null` tells us that a child does not exist.

---

## ⚙️ Algorithm

### Serialization

```text
serialize(root):

1. If root is None:
      store "null"
2. Otherwise:
      store root.val
      serialize(root.left)
      serialize(root.right)
3. Join all values using ","
```

### Deserialization

```text
deserialize(data):

1. Split data using ","
2. Start from index = 0
3. If current value is "null":
      move index
      return None
4. Create a node using current value
5. Build left subtree recursively
6. Build right subtree recursively
7. Return the node
```

---

## ⏱️ Complexity

Let `n` be the number of nodes.

* **Time:** `O(n)`
* **Space:** `O(n)`

Every node is visited once during serialization and once during deserialization.

---

## 🔑 Key Insight

Preorder values alone are **not enough** to reconstruct a binary tree.

For example:

```text
    1          1
   /            \
  2              2
```

Both can have:

```text
1,2
```

as preorder.

Therefore, we also store `null` values:

```text
1,2,null,null,null
```

vs.

```text
1,null,2,null,null
```

Now the structure can be uniquely reconstructed.

---

## 📝 Important Concept

```text
Binary Tree
     ↓
Preorder DFS
     ↓
Values + NULL markers
     ↓
Serialized String
     ↓
Split into values
     ↓
Preorder Reconstruction
     ↓
Original Binary Tree
```

### Key Takeaway

> **Preo**
