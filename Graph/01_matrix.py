from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        if not mat:
            return []
        rows = len(mat)
        cols = len(mat[0])
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1),   # Right
        ]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx = dx + x
                ny = dy + y
                if 0<=nx<rows and 0<=ny<cols:
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx,ny))

        return dist
