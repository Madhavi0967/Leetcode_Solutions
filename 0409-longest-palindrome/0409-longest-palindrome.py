class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts={}
        for char in s:
            char_counts[char]=char_counts.get(char,0)+1
        length=0
        has_odd = False
        for count in char_counts.values():
            if count%2==0:
                length+=count
            else:
                length+=count-1
                has_odd = True
        if has_odd:
            length+=1
        return length
