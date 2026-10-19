class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2

        # 1. Find pivot
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Find next greater element and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse the remaining suffix
        nums[i + 1:] = reversed(nums[i + 1:])
