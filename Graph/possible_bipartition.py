
from collections import deque
from typing import List


class Solution:
    def possibleBipartition(
        self, n: int, dislikes: List[List[int]]
    ) -> bool:

        # Build adjacency list
        graph = [[] for _ in range(n + 1)]

        for person_a, person_b in dislikes:
            graph[person_a].append(person_b)
            graph[person_b].append(person_a)

        # -1 means uncolored
        color = [-1] * (n + 1)

        # Handle disconnected components
        for person in range(1, n + 1):

            if color[person] != -1:
                continue

            queue = deque([person])
            color[person] = 0

            while queue:
                current = queue.popleft()

                for neighbor in graph[current]:

                    # Same color means conflict
                    if color[neighbor] == color[current]:
                        return False

                    # Assign opposite color
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)

        return True