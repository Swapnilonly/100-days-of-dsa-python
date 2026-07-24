class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxarea = 0

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                top = stack.pop()
                height = heights[top]

                if stack:
                    left = stack[-1]
                else:
                    left = -1

                width = i - left - 1

                maxarea = max(maxarea, height * width)

            stack.append(i)

        return maxarea






