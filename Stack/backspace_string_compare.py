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


    ####  Optimal approach  #####

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        i = len(s) - 1
        j = len(t) - 1

        skipS = 0
        skipT = 0

        while i >= 0 or j >= 0:

            # Find next valid character in s
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            # Find next valid character in t
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            # Compare characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True