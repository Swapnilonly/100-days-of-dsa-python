class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = {}
        ans = []
        stack = []
        # calculate nextgtr for every element in nums2
        for i in range(n - 1, -1, -1):

            # checking top element is less than current
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            # Checking if next greater element found
            if stack and stack[-1] > nums2[i]:
                res[nums2[i]] = stack[-1]

            # If no elements add -1 as next greater element
            else:
                res[nums2[i]] = -1

            stack.append(nums2[i])
        # cmpute result
        for j in range(len(nums1)):
            ans.append(res[nums1[j]])

        return ans






