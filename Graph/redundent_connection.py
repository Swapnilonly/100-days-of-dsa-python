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

# OPTIMIZED AND UNDERSTANDABLE APPROACH
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])

            return parent[u]

        # calculate default parent and size

        for u, v in edges:
            pu = find(u)
            pv = find(v)

            # check redundent edge
            if pu == pv:
                return [u, v]

            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]

            elif size[pv] < size[pu]:
                parent[pv] = pu
                size[pu] += size[pv]

            else:
                parent[pv] = pu
                size[pu] += size[pv]

        return []
