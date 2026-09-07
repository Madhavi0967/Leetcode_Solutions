class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0
        for num in nums:
            if num == 1:
                current_consecutive += 1
            else:
                # max_consecutive max(max_consecutive, current_consecutive)
                current_consecutive = 0
            max_consecutive = max(max_consecutive,current_consecutive)
        return max_consecutive