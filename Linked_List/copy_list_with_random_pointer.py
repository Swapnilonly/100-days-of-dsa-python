"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        # copying the node in hashmap
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        # connecting next and random
        curr = head
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap.get(curr.next)
            copy.random = hashmap.get(curr.random)

            curr = curr.next
        return hashmap.get(head)

