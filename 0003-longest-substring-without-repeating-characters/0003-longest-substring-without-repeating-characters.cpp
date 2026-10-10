class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> seen;
        int maxLen = 0, start = 0;

        for (int end = 0; end < s.length(); ++end) {
            char c = s[end];
            if (seen.count(c) && seen[c] >= start) {
                start = seen[c] + 1;  // Move start to avoid duplicate
            }
            seen[c] = end;
            maxLen = max(maxLen, end - start + 1);
        }

        return maxLen;

    }
};