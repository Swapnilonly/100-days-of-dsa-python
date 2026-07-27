class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            # Remove larger digits from the stack
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If removals are still left, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Convert list to string
        result = "".join(stack)

        # Remove leading zeros
        result = result.lstrip("0")

        # If the string becomes empty, return "0"
        return result if result else "0"