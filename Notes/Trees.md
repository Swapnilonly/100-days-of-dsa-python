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