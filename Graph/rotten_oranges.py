from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        fresh_oranges = 0

        self._initialize_grid(grid, queue)

        for row in grid:
            fresh_oranges += row.count(1)

        minutes = 0

        while queue and fresh_oranges:
            fresh_oranges, minutes = self._process_minute(
                grid,
                queue,
                fresh_oranges,
                minutes,
            )

        return -1 if fresh_oranges else minutes

    def _initialize_grid(
        self,
        grid: list[list[int]],
        queue: deque,
    ) -> None:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))

    def _process_minute(
        self,
        grid: list[list[int]],
        queue: deque,
        fresh_oranges: int,
        minutes: int,
    ) -> tuple[int, int]:
        current_level_size = len(queue)

        for _ in range(current_level_size):
            row, col = queue.popleft()

            for next_row, next_col in self._get_neighbors(
                row, col, grid
            ):
                if grid[next_row][next_col] != 1:
                    continue

                grid[next_row][next_col] = 2
                fresh_oranges -= 1
                queue.append((next_row, next_col))

        return fresh_oranges, minutes + 1

    def _get_neighbors(
        self,
        row: int,
        col: int,
        grid: list[list[int]],
    ) -> list[tuple[int, int]]:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = []

        for row_change, col_change in (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ):
            next_row = row + row_change
            next_col = col + col_change

            if 0 <= next_row < rows and 0 <= next_col < cols:
                neighbors.append((next_row, next_col))

        return neighbors