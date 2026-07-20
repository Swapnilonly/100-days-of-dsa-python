class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i].isdigit():
                stack.append(int(operations[i]))

            elif operations[i] == 'C':
                stack.pop()

            elif operations[i] == 'D':
                stack.append(stack[-1] * 2)

            elif operations[i] == '+':
                stack.append(stack[-1] + stack[-2])

        return sum(stack)



####### Clean Code #######

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            try:
                stack.append(int(op))
            except ValueError:
                if op == "C":
                    stack.pop()
                elif op == "D":
                    stack.append(stack[-1] * 2)
                elif op == "+":
                    stack.append(stack[-1] + stack[-2])

        return sum(stack)


########  Optimized Code  ######

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in operations:
            if(i=='C'):
                l.pop()
            elif(i=='D'):
                l.append(l[-1]*2)
            elif(i=='+'):
                l.append(l[-1]+l[-2])
            else:
                l.append(int(i))
        return sum(l)

