class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}

        def dfs(val):
            for i in graph[val]:
                if i in color:
                    if color[i] == color[val]:
                        return False
                else:
                    color[i] = 1 - color[val]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True

