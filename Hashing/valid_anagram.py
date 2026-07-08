class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1
        return all(value == 0 for value in freq.values())





