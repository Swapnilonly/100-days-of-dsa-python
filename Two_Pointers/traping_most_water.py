

 ######  APPROACH USING PREFIX AND SUFFIX MAXIMUM  #############


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = height[0]
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i])

        rightmax[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            rightmax[j] = max(rightmax[j + 1], height[j])
        water = 0

        for k in range(n):
            water += min(leftmax[k], rightmax[k]) - height[k]
        return water



###########   TWO POINTER APPROACH   ##############

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water


