class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = '+'
        num = 0
        for i in range(len(s) + 1):
            ch = '+' if i == len(s) else s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch != ' ':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    num2 = stack.pop()
                    stack.append(int(num2 * num))

                elif op == '/':
                    stack.append(int(stack.pop() / num))
                op = ch
                num = 0
        res = 0
        while stack:
            res += stack.pop()
        return res

