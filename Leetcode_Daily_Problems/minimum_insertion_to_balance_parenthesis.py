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



# OPTIMAL SOLUTION
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0
        index = 0

        while index < len(s):
            if s[index] == '(':
                open_needed += 1

            else:
                # A closing pair must be ))
                if index + 1 < len(s) and s[index + 1] == ')':
                    index += 1
                else:
                    # Insert the missing closing parenthesis
                    insertions += 1

                if open_needed > 0:
                    open_needed -= 1
                else:
                    # Insert a missing opening parenthesis
                    insertions += 1

            index += 1

        # Each remaining opening parenthesis needs two ')'
        insertions += open_needed * 2

        return insertions