# 🔗 Linked List Implementation

A **Linked List** is a linear data structure where elements are stored in separate nodes. Each node contains:

- `data` → stores the value
- `next` → stores a reference to the next node

In a **Singly Linked List**, each node points only to the next node.

---

## 📌 Structure

```text
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