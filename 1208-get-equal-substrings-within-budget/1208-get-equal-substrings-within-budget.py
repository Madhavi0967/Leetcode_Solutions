class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        total_cost = 0
        max_len = 0

        for right in range(len(s)):
            total_cost += abs(ord(s[right]) - ord(t[right]))

            while total_cost > maxCost:
                total_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len