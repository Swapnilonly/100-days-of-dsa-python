class Solution:
    def canFinish(self, n: int, edges: list[list[int]]) -> bool:
        recpath = [False] * n
        vis = [False] * n

        def dfs(src, recpath, vis, edges):
            vis[src] = True
            recpath[src] = True

            for i in range(len(edges)):
                v = edges[i][0]
                u = edges[i][1]

                if u == src:
                    if not vis[v]:
                        if dfs(v, recpath, vis, edges):
                            return True

                    elif recpath[v]:
                        return True

            recpath[src] = False

            return False

        for i in range(n):
            if not vis[i]:
                if dfs(i, recpath, vis, edges):
                    return False

        return True
