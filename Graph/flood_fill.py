class Solution:
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]

        # If the color is already the same
        if original_color == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Only fill cells having the original color
            if image[r][c] != original_color:
                return

            # Change the color
            image[r][c] = color

            # Visit 4 adjacent cells
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        dfs(sr, sc)

        return image