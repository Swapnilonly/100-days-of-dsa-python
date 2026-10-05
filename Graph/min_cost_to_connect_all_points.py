class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        min_cost = [float("inf")] * n
        visited = [False] * n

        min_cost[0] = 0
        total_cost = 0

        for _ in range(n):
            # Find the unvisited point with minimum connection cost
            current = -1

            for i in range(n):
                if not visited[i] and (
                    current == -1 or min_cost[i] < min_cost[current]
                ):
                    current = i

            # Add current point to MST
            visited[current] = True
            total_cost += min_cost[current]

            # Update connection costs
            x1, y1 = points[current]

            for i in range(n):
                if visited[i]:
                    continue

                x2, y2 = points[i]
                distance = abs(x1 - x2) + abs(y1 - y2)

                min_cost[i] = min(min_cost[i], distance)

        return total_cost