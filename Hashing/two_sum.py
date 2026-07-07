class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in check:
                return check[temp], i
            else:
                check[nums[i]] = i






