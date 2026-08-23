class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = None
        self.tail = None

    # Add node at the beginning
    def add_to_head(self, node):

        # Empty list
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node

        self.head = node

    # Remove a node from the list
    def remove_node(self, node):

        # Node is the only node
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None

        # Node is head
        elif node == self.head:
            self.head = node.next
            self.head.prev = None

        # Node is tail
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        # Node is somewhere in the middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = None

    # Move an existing node to head
    def move_to_head(self, node):

        if node == self.head:
            return

        self.remove_node(node)
        self.add_to_head(node)

    def get(self, key: int) -> int:

        # Key doesn't exist
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Recently used -> move to head
        self.move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:

            node = self.cache[key]

            # Update value
            node.value = value

            # Make it most recently used
            self.move_to_head(node)

            return

        # Create new node
        new_node = Node(key, value)

        # Add to hashmap
        self.cache[key] = new_node

        # Add to head
        self.add_to_head(new_node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:

            # Remove least recently used node
            lru_node = self.tail

            self.remove_node(lru_node)

            # Remove from hashmap
            del self.cache[lru_node.key]