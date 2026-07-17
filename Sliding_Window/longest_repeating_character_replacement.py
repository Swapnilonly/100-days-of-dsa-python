class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        freq = {}
        maxfreq = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxfreq = max(maxfreq, freq[s[r]])
            if (r - l + 1) - maxfreq > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            res = max(r - l + 1, res)
        return res


