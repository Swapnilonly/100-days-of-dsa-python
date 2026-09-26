from typing import List


class Solution:
    def pacificAtlantic(
        self, heights: List[List[int]]
    ) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        def dfs(row, col, visited):
            visited.add((row, col))

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if not (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                ):
                    continue

                if (new_row, new_col) in visited:
                    continue

                if (
                    heights[new_row][new_col]
                    < heights[row][col]
                ):
                    continue

                dfs(new_row, new_col, visited)

        # Pacific: top and left boundaries
        for col in range(cols):
            dfs(0, col, pacific)

        for row in range(rows):
            dfs(row, 0, pacific)

        # Atlantic: bottom and right boundaries
        for col in range(cols):
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            dfs(row, cols - 1, atlantic)

        # Cells reachable from both oceans
        result = []

        for row in range(rows):
            for col in range(cols):
                if (
                    (row, col) in pacific
                    and (row, col) in atlantic
                ):
                    result.append([row, col])

        return result