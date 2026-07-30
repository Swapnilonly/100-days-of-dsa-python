class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        check = [False] * 26
        last = [0] * 26
        stack = []

        # Store the last occurrence of each character
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')

            # If character is already in stack, skip it
            if check[idx]:
                continue

            # Maintain increasing lexicographical order
            while (
                stack
                and stack[-1] > ch
                and last[ord(stack[-1]) - ord('a')] > i
            ):
                removed = stack.pop()
                check[ord(removed) - ord('a')] = False

            stack.append(ch)
            check[idx] = True

        return ''.join(stack)