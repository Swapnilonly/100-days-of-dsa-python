class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            alive = True
            while stack and (asteroids[i] < 0 and stack[-1] > 0):
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()

                elif abs(stack[-1]) > abs(asteroids[i]):
                    alive = False
                    break

                else:
                    stack.pop()
                    alive = False
                    break

            if alive:
                stack.append(asteroids[i])

        return stack



