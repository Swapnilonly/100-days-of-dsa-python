class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            # u and v are already connected
            if root_u == root_v:
                return [u, v]

            # Union the two components
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

        return []