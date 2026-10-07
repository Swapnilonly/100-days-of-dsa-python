class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        size = [1] * n
        components = n

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for u, v in connections:
            root_u = find(u)
            root_v = find(v)

            # Same root means this cable is redundant.
            if root_u == root_v:
                continue

            # Attach the smaller component to the larger one.
            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u

            parent[root_v] = root_u
            size[root_u] += size[root_v]

            # Two components are merged into one.
            components -= 1

        return components - 1