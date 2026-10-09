class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        insertion = 0
        idx = 0
        n = len(s)

        while idx < n:
            if s[idx] == "(":
                stack.append("(")

            else:
                # Check whether we have a complete ))
                if idx + 1 < n and s[idx + 1] == ")":
                    idx += 1

                else:
                    insertion += 1

                # Match the closing pair with an opening (
                if stack:
                    stack.pop()

                else:
                    insertion += 1

            idx += 1

        return insertion + len(stack) * 2



