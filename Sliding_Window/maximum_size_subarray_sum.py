
######  VARIABLE LENGTH SLIDING WINDOW  ############

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        csum = 0
        res = float('inf')
        for r in range(len(nums)):
            csum += nums[r]
            while csum >= target:
                res = min(res, r - l + 1)
                csum -= nums[l]
                l += 1
        return 0 if res == float('inf') else res









