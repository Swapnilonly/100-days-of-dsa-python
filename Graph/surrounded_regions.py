from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Modify the board in-place by capturing surrounded regions.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def mark_safe(row: int, col: int) -> None:
            stack = [(row, col)]
            board[row][col] = "#"

            while stack:
                current_row, current_col = stack.pop()

                directions = [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0)
                ]

                for row_change, col_change in directions:
                    new_row = current_row + row_change
                    new_col = current_col + col_change

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and board[new_row][new_col] == "O"
                    ):
                        board[new_row][new_col] = "#"
                        stack.append((new_row, new_col))

        # Step 1: Traverse the first and last columns.
        for row in range(rows):
            if board[row][0] == "O":
                mark_safe(row, 0)

            if board[row][cols - 1] == "O":
                mark_safe(row, cols - 1)

        # Step 2: Traverse the first and last rows.
        for col in range(cols):
            if board[0][col] == "O":
                mark_safe(0, col)

            if board[rows - 1][col] == "O":
                mark_safe(rows - 1, col)

        # Step 3: Capture surrounded regions and restore safe cells.
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"