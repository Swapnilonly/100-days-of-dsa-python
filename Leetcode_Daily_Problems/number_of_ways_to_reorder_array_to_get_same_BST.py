
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        combinations = [[0] * (n + 1) for _ in range(n + 1)]

        for row in range(n + 1):
            combinations[row][0] = 1
            combinations[row][row] = 1

            for col in range(1, row):
                combinations[row][col] = (
                    combinations[row - 1][col - 1]
                    + combinations[row - 1][col]
                ) % MOD

        def count_orders(values: list[int]) -> int:
            if len(values) <= 1:
                return 1

            root = values[0]
            left = [value for value in values[1:] if value < root]
            right = [value for value in values[1:] if value > root]

            left_ways = count_orders(left)
            right_ways = count_orders(right)

            interleavings = combinations[len(values) - 1][len(left)]

            return (
                interleavings * left_ways % MOD * right_ways % MOD
            )

        return (count_orders(nums) - 1) % MOD
