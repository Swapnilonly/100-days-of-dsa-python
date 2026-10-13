class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(num * num for num in nums)
        mid = len(nums) // 2
        neg = sum(sq[:mid])
        pos = sum(sq[mid:])

        return pos - neg
