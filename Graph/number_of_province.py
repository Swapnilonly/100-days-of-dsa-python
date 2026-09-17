class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city):
            visited[city] = True

            for neighbor in range(n):
                if isConnected[city][neighbor] == 1:
                    if not visited[neighbor]:
                        dfs(neighbor)

        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces