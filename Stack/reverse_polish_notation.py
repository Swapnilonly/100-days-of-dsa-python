class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1. traverse through each tokens
        # 2. if the token is a number or operand push into the stack
        # 3. elif any operator found pop last two element from the stack and perform operation and add result in stack
        # 4. Repeat untill all element get traversed
        # 5. return the result
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                f = stack.pop()
                s = stack.pop()
                res = 0
                if tokens[i] == '+':
                    res = s + f
                elif tokens[i] == '-':
                    res = s - f
                elif tokens[i] == '*':
                    res = s * f
                elif tokens[i] == '/':
                    res = s / f
                stack.append(int(res))
            else:
                stack.append(int(tokens[i]))

        return stack[-1]


#####  OPTIMIZED SOLUTION USING LAMBDA FUNCTION APPROACH  #####

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        stack = []

        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))

        return stack[-1]
