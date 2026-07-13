class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = "".join(ch.lower() for ch in s if ch.isalnum())
        if c == c[::-1]:
            return True
        return False
