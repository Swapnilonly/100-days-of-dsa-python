from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 32

        # Count how many numbers have each bit set
        for num in nums:
            for bit in range(32):
                if num & (1 << bit):
                    bit_count[bit] += 1

        answer = 0

        # Build k maximum possible numbers
        for _ in range(k):
            num = 0

            for bit in range(32):
                if bit_count[bit] > 0:
                    num |= 1 << bit
                    bit_count[bit] -= 1

            answer = (answer + num * num) % MOD

        return answer