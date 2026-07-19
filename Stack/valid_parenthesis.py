class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for ch in s:

            # Opening bracket
            if ch not in check:
                stack.append(ch)

            # Closing bracket
            else:
                if not stack:
                    return False

                if stack[-1] != check[ch]:
                    return False

                stack.pop()

        return len(stack) == 0