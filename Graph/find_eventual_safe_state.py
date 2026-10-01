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



