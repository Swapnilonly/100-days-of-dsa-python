class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        if not graph:
            return []
        safenode = set()
        # find the terminals first
        for i in range(len(graph)):
            if not graph[i]:
                safenode.add(i)

        status = True
        while status:
            status = False
            for j in range(len(graph)):
                if j in safenode:
                    continue

                if all(nb in safenode for nb in graph[j]):
                    safenode.add(j)
                    status = True

        return sorted(safenode)


#  OPTIMIZED APPROACH

from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        outdegrees = []
        safenodes = []

        # calculate outdegrees for each nodes
        for i in graph:
            outdegrees.append(len(i))

        queue = deque([])

        # check if outdegree of a node is 0 add them into the queue
        for j in range(n):
            if outdegrees[j] == 0:
                queue.append(j)

        # reverse the graph
        rev_graph = self.reverse_graph(graph)

        # traverse the graph through bfs traversal on terminal nodes
        while queue:
            node = queue.popleft()
            safenodes.append(node)

            for i in rev_graph[node]:
                outdegrees[i] -= 1
                if outdegrees[i] == 0:
                    queue.append(i)

        return sorted(safenodes)

    def reverse_graph(self, graph):
        n = len(graph)
        rev = [[] for _ in range(n)]

        for node, nbrs in enumerate(graph):
            for nb in nbrs:
                rev[nb].append(node)

        return rev






