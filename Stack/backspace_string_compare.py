##### My Approach  #######

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []

        for i in t:
            if i == "#":
                if a:
                    a.pop()
            else:
                a.append(i)
        for j in s:
            if j == "#":
                if b:
                    b.pop()
            else:
                b.append(j)

        return a == b


########   DO NOT REPEAT APPROACH   ##########

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(t):
            a = []
            for i in t:
                if i == "#":
                    if a:
                        a.pop()
                else:
                    a.append(i)

            return a

        return check(s) == check(t)

