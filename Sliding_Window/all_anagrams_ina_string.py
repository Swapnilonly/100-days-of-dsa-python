from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str):

        l = 0
        window = defaultdict(int)
        count = defaultdict(int)
        res = []

        # pattern frequency
        for ch in p:
            count[ch] += 1

        for r in range(len(s)):

            # add current character
            window[s[r]] += 1

            # shrink window if it becomes larger
            if r - l + 1 > len(p):

                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]

                l += 1

            # compare
            if window == count:
                res.append(l)

        return res