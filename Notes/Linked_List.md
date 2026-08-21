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



## Problem

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the result as a linked list.

### Example

    Input:
    l1 = 2 → 4 → 3
    l2 = 5 → 6 → 4

    Output:
    7 → 0 → 8

Explanation:

    l1 represents 342
    l2 represents 465

    342 + 465 = 807

    Result:
    7 → 0 → 8

---

## Approach: Traverse + Add + Carry

The solution uses three important linked-list techniques:

1. Traverse both linked lists simultaneously
2. Add corresponding digits with carry
3. Build the result list using a dummy node

### Step 1: Traverse Both Lists

Use two pointers to traverse both linked lists.

    l1: 2 → 4 → 3
        ↑
      temp1

    l2: 5 → 6 → 4
        ↑
      temp2

Continue while at least one list still has a node.

If one list is shorter, treat its missing value as `0`.

    val1 = temp1.val if temp1 else 0
    val2 = temp2.val if temp2 else 0

### Step 2: Add Digits and Handle Carry

Add the current digits along with the previous carry.

    sum = val1 + val2 + carry

Calculate the current digit:

    digit = sum % 10

Calculate the carry for the next position:

    carry = sum // 10

Example:

    9 + 8 = 17

    digit = 7
    carry = 1

The carry is added to the next addition.

### Step 3: Build the Result List

Create a new node using the calculated digit and attach it to the result list.

    l1:      2 → 4 → 3
    l2:      5 → 6 → 4

              ↓

    Result:   7 → 0 → 8

If a carry is still left after both lists are exhausted, add one final node.

Example:

    l1 = 9 → 9
    l2 = 9 → 9

    9 + 9 = 18
    9 + 9 + 1 = 19

    Result:
    8 → 9 → 1

---

## Edge Case

For lists with different lengths, treat the missing digits as `0`.

Example:

    l1 = 2 → 4 → 3
    l2 = 5 → 6

    Output:
    7 → 0 → 3

If a carry remains after processing both lists, add it as the final node.

Example:

    l1 = 9
    l2 = 9

    Output:
    8 → 1

---

## Complexity

### Time Complexity

    O(N)

The linked lists are traversed once, where `N` is the length of the longer list.

### Space Complexity

    O(N)

The result linked list requires up to `N + 1` nodes because of a possible final carry.

---

## Key Takeaway

For the optimal approach:

    1. Traverse both lists
    2. Get the current values
    3. Add values with carry
    4. Store the current digit
    5. Update the carry
    6. Move both pointers
    7. Add the final carry if required

The important pattern is:

    Traverse → Add → Carry → Build

---

## Pattern

**Linked List → Simultaneous Traversal → Carry Handling → Dummy Node → Result List**



# 138. Copy List with Random Pointer

**LeetCode:** 138
**Difficulty:** Medium
**Topic:** Linked List, HashMap, Deep Copy

---

## Problem

Given a linked list where each node has:

* `val`
* `next`
* `random`

The `random` pointer can point to **any node** in the list or `None`.

Create a **deep copy** of the linked list.

---

## Example

```text
Original:

7 → 13 → 11 → 10 → 1
↓    ↓     ↓     ↓    ↓
-    7     1    11    7


Copy:

7' → 13' → 11' → 10' → 1'
↓     ↓      ↓      ↓     ↓
-     7'     1'    11'    7'
```

The copied nodes must be completely independent of the original nodes.

---

## Approach

### 1. Create Copies

Traverse the original linked list and create a new node for every node.

Store the relationship in a HashMap:

```text
Original Node → Copied Node
```

Example:

```text
7  → 7'
13 → 13'
11 → 11'
```

### 2. Connect `next` and `random`

Traverse the list again.

For every original node:

```text
copy.next   = copied version of curr.next
copy.random = copied version of curr.random
```

The HashMap lets us find the copied node in `O(1)` average time.

### 3. Return the Copied Head

```text
hashmap.get(head)
```

---

## Edge Cases

* `head = None`
* Single node
* `random = None`
* `random` points to itself
* `random` points to any other node

---

## Complexity

**Time:** `O(n)`
Two traversals of the linked list.

**Space:** `O(n)`
HashMap stores every original-to-copy relationship.

---

## Key Takeaway

The main pattern is:

```text
Original Node → Copied Node
```

Use a **HashMap** when copied nodes need to maintain relationships with other copied nodes.

```text
Pass 1 → Create all nodes
Pass 2 → Connect next + random
```

---

## Pattern

**HashMap + Linked List → Deep Copy**

This pattern is useful when nodes have complex relationships such as:

```text
next
random
parent
neighbors
```

---