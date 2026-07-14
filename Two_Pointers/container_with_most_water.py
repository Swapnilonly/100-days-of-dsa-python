class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        n = len(height)
        r = n - 1
        l = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            maxx = max(maxx, w * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxx
