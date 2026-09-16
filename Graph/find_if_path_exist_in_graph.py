from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        # 1. Create adjacency list
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 2. BFS initialization
        queue = deque([source])
        visited = {source}

        # 3. Traverse the graph
        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False