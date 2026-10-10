from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        result = []
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return result

        target = Counter(words)

        for i in range(word_len):
            left = i
            seen = {}
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > target[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == word_count:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return result