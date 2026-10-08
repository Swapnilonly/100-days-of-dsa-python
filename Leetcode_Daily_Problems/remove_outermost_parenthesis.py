class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for parenthesis in s:
            if parenthesis == '(':
                if depth > 0:
                    result.append(parenthesis)
                depth += 1

            else:
                depth -= 1
                if depth > 0:
                    result.append(parenthesis)

        return ''.join(result)