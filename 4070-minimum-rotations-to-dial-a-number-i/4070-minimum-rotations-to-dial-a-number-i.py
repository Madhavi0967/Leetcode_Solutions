class Solution:
    def minRotations(self, s: str) -> int:
        current=0
        total=0
        for ch in s:
            digit=int(ch)
            diff = abs(digit-current)
            rotations = min(diff,10-diff)
            total+=rotations
            current=digit
        return total