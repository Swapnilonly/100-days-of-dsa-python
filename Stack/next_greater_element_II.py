class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1]*n
        for j in range((2*n)-1, -1, -1):
            i = j%n
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]

            stack.append(nums[i])

        return res



