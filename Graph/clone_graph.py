"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])
        clones = {node: Node(node.val)}
        while queue:
            current = queue.popleft()
            for n in current.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)
                    queue.append(n)

                clones[current].neighbors.append(clones[n])

        return clones[node]


