class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = Counter(s)
        sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
        result =[]
        for char, count in sorted_chars:
            result.append(char * count)
        return "".join(result)