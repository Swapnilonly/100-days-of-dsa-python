class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                summ += nums[i] ** 2

        return summ

