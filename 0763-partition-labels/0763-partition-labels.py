class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurence={}
        for i, char in enumerate(s):
            last_occurence[char]=i
        result =[]
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end,last_occurence[char])
            if i == end:
                result.append(end-start+1)
                start = i+1
        return result