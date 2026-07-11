class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = {}
        maxx = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in lst:
                lst.add(s[i])
                maxx = max(i - l + 1, maxx)
            while s[i] in lst:
                lst.remove(s[l])
                l += 1
        return maxx



