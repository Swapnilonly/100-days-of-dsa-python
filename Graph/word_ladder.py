class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for index in range(len(word)):
                for char_code in range(ord("a"), ord("z") + 1):
                    new_char = chr(char_code)

                    if new_char == word[index]:
                        continue

                    transformed_word = (
                            word[:index] + new_char + word[index + 1:]
                    )

                    if transformed_word in word_set:
                        queue.append((transformed_word, length + 1))
                        word_set.remove(transformed_word)

        return 0


