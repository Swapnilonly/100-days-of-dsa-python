class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = set()
        maxx = 0
        l = 0
        for i in range(len(s)):
            while s[i] in lst:
                lst.remove(s[l])
                l += 1
            lst.add(s[i])
            maxx = max(i - l + 1, maxx)
        return maxx



