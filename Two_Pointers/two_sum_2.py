class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        n = len(numbers)
        r = n - 1

        while l < n and l < r:
            csum = numbers[l] + numbers[r]
            if csum == target:
                return [l + 1, r + 1]
            elif csum > target:
                r -= 1
            elif csum < target:
                l += 1

