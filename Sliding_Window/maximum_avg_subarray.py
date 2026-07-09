class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        maxx = float('-inf')
        csum = 0
        for r in range(len(nums)):
            csum += nums[r]
            if r - l + 1 == k:
                maxx = max(csum, maxx)
                csum -= nums[l]
                l += 1
        return maxx / k




