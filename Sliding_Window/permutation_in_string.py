from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer than s2, it's impossible
        if len(s1) > len(s2):
            return False

        # Frequency of characters in s1
        target = Counter(s1)

        # Frequency of the current window in s2
        window = Counter()

        left = 0

        # Expand the window
        for right in range(len(s2)):

            # Add current character to the window
            window[s2[right]] += 1

            # Keep the window size equal to len(s1)
            if right - left + 1 > len(s1):

                window[s2[left]] -= 1

                # Remove the key if its count becomes 0
                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            # If both frequency maps are the same,
            # current window is a permutation of s1
            if window == target:
                return True

        return False