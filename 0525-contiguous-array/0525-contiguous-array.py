class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}
        balance = 0
        max_len = 0

        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            if balance in first_index:
                max_len = max(max_len, i - first_index[balance])
            else:
                first_index[balance] = i

        return max_len