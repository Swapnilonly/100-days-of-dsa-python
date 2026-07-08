# KADANA'S ALGORITHM

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        csum = nums[0]
        for i in range(1, len(nums)):
            csum = max(nums[i], csum + nums[i])
            maxx = max(csum, maxx)
        return maxx




