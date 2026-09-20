class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row: int, col: int) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row, col))

            area = 1

            area += dfs(row - 1, col)
            area += dfs(row + 1, col)
            area += dfs(row, col - 1)
            area += dfs(row, col + 1)

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    island_area = dfs(row, col)
                    max_area = max(max_area, island_area)

        return max_area