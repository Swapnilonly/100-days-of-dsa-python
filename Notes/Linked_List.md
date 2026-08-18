# 🔗 Linked List Implementation

A **Linked List** is a linear data structure where elements are stored in separate nodes. Each node contains:

- `data` → stores the value
- `next` → stores a reference to the next node

In a **Singly Linked List**, each node points only to the next node.

---

## 📌 Structure

head
 ↓
[10 | next] → [20 | next] → [30 | None]

...

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" → ")
            current = current.next

        print("None")


ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.insert_at_beginning(5)

ll.display()


# 🔗 141. Linked List Cycle

**LeetCode:** [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

## 📌 Problem

Given the head of a linked list, determine if the linked list contains a cycle.

A cycle exists when a node's `next` pointer points to a previous node in the linked list.

---

## 💡 Approach

### Floyd's Cycle Detection Algorithm

Use two pointers:

- `slow` → moves one step at a time
- `fast` → moves two steps at a time

### Steps

1. Initialize `slow` and `fast` at `head`.
2. If `head` is `None`, return `False`.
3. Move `slow` one step.
4. Move `fast` two steps.
5. If `slow == fast`, a cycle exists.
6. If `fast` or `fast.next` becomes `None`, no cycle exists.

---

# 19. Remove Nth Node From End of List

**LeetCode:** [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

**Difficulty:** Medium

**Topic:** Linked List

---

## Problem

Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

### Example

```text
Input:
1 → 2 → 3 → 4 → 5
n = 2

Output:
1 → 2 → 3 → 5
```

---

## Approach: Two Pass

The solution uses two traversals of the linked list.

### Step 1: Count the Nodes

Traverse the complete linked list and calculate its length.

```text
1 → 2 → 3 → 4 → 5

count = 5
```

### Step 2: Find the Previous Node

The position of the node to remove from the beginning is:

```text
count - n
```

For:

```text
count = 5
n = 2

target = 5 - 2
       = 3
```

So we reach the node just before the node that needs to be removed.

### Step 3: Remove the Node

Once we reach the previous node:

```text
head2.next = head2.next.next
```

This skips the target node.

```text
Before:

3 → 4 → 5

After:

3 → 5
```

---

## Edge Case

If:

```text
count == n
```

the node to remove is the **head node**.

Example:

```text
1 → 2 → 3
n = 3
```

Return:

```text
2 → 3
```

---

## Complexity

### Time Complexity

```text
O(N)
```

The linked list is traversed twice.

### Space Complexity

```text
O(1)
```

Only a few pointer variables are used.

---

## Key Takeaway

For the two-pass approach:

```text
1. Count the total nodes
2. Handle head-removal case
3. Find the node before the target
4. Skip the target node
```

The important linked-list operation is:

```python
current.next = current.next.next
```

which removes a node by bypassing it.

---

## Pattern

**Linked List → Two Pass Traversal → Pointer Manipulation**

---

### Word of the Day

**Bypass** — to skip something or go around it.

In this problem, `current.next = current.next.next` **bypasses** the node that needs to be removed.



# 143. Reorder List

**LeetCode:** [Reorder List](https://leetcode.com/problems/reorder-list/)

**Difficulty:** Medium

**Topic:** Linked List

---

## Problem

Given the head of a singly linked list, reorder the list in the following pattern:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

The list must be modified **in-place**.

### Example

    Input:
    1 → 2 → 3 → 4 → 5

    Output:
    1 → 5 → 2 → 4 → 3

---

## Approach: Middle + Reverse + Merge

The solution uses three important linked-list techniques:

1. Find the middle of the linked list
2. Reverse the second half
3. Merge both halves alternately

### Step 1: Find the Middle

Use the **slow and fast pointer** technique.

    1 → 2 → 3 → 4 → 5
            ↑
           slow

Split the list:

    First Half:
    1 → 2 → 3

    Second Half:
    4 → 5

### Step 2: Reverse the Second Half

Reverse:

    4 → 5

into:

    5 → 4

Now:

    First Half:   1 → 2 → 3
    Second Half:  5 → 4

### Step 3: Merge Both Halves

Take nodes alternately from both halves:

    1 → 5 → 2 → 4 → 3

---

## Edge Case

For lists with one or two nodes, no reordering is required.

Example:

    1 → 2

Output:

    1 → 2

---

## Complexity

### Time Complexity

    O(N)

The linked list is traversed for finding the middle, reversing the second half, and merging both halves.

### Space Complexity

    O(1)

Only a few pointer variables are used and the list is modified in-place.

---

## Key Takeaway

For the optimal approach:

    1. Find the middle
    2. Split the list
    3. Reverse the second half
    4. Merge both halves alternately

The important pattern is:

    Middle → Reverse → Merge

---

## Pattern

**Linked List → Fast & Slow Pointers → Reverse Linked List → Merge**

---

### Word of the Day

**Interleave** — to combine two sequences by alternating their elements.

In this problem, the two halves are **interleaved**:

    1 → 5 → 2 → 4 → 3


Intersection of Two Linked Lists

LeetCode: 160. Intersection of Two Linked Lists
Difficulty: Easy
Topic: Linked List, Two Pointers

Problem

Given the heads of two singly linked lists, return the node at which the two linked lists intersect.

If the two linked lists do not intersect, return None.

Important: Intersection means the same node/object, not just the same value.

Example
List A:  4 → 1 ──→ 8 → 4 → 5
                    ↑
                    │
List B:  5 → 6 → 1 ─┘


Intersection Node = 8

Here, both lists point to the same ListNode object containing 8.

Approach
1. Calculate the length of both lists
List A:  4 → 1 → 8 → 4 → 5
Length = 5


List B:  5 → 6 → 1 → 8 → 4 → 5
Length = 6
2. Find the difference
Difference = |5 - 6| = 1
3. Move the pointer of the longer list ahead
List A:  4 → 1 → 8 → 4 → 5
              ↑


List B:  5 → 6 → 1 → 8 → 4 → 5
              ↑

Now both pointers are at the same relative position from the end.

4. Move both pointers together
h1 → 8
h2 → 8

Check:

if h1 is h2:

If True, we found the intersection node.

Why is instead of ==?

is checks object identity.