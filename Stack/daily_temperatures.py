## Optimal Solution  ####

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        # Initialize answer array with 0
        answer = [0] * n

        # Stack will store indices of temperatures
        stack = []

        for i in range(n):

            # If current temperature is greater than the temperature
            # at the index on top of the stack,
            # then we found the next warmer day.
            while stack and temperatures[i] > temperatures[stack[-1]]:

                prev_index = stack.pop()

                # Distance between current day and previous day
                answer[prev_index] = i - prev_index

            # Push current index into the stack
            stack.append(i)

        return answer