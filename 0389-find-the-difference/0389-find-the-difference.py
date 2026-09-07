class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for char in t:
            if char not in count or count[char]==0:
                return char
            else:
                count[char]-=1