from heapq import heappush, heappop


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])

        efforts = [[float("inf")] * columns for _ in range(rows)]
        efforts[0][0] = 0

        min_heap = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            current_effort, row, column = heappop(min_heap)

            if (row, column) == (rows - 1, columns - 1):
                return current_effort

            if current_effort > efforts[row][column]:
                continue

            for dr, dc in directions:
                new_row = row + dr
                new_column = column + dc

                if not (0 <= new_row < rows and 0 <= new_column < columns):
                    continue

                difference = abs(
                    heights[row][column] - heights[new_row][new_column]
                )

                new_effort = max(current_effort, difference)

                if new_effort < efforts[new_row][new_column]:
                    efforts[new_row][new_column] = new_effort
                    heappush(
                        min_heap,
                        (new_effort, new_row, new_column),
                    )

        return 0