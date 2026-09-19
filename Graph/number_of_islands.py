class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def dfs(row, col):
            # Boundary check
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # Water or already visited
            if grid[row][col] == "0" or (row, col) in visited:
                return

            # Mark as visited
            visited.add((row, col))

            # Explore 4 directions
            dfs(row - 1, col)  # top
            dfs(row + 1, col)  # bottom
            dfs(row, col - 1)  # left
            dfs(row, col + 1)  # right

        # Scan every cell
        for row in range(rows):
            for col in range(cols):

                # Found a new island
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)

        return islands