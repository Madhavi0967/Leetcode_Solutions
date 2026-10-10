class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)

        left = 0
        right = n - 1

        while left < n and nums[left] == sorted_nums[left]:
            left += 1

        while right >= 0 and nums[right] == sorted_nums[right]:
            right -= 1

        if left >= right:
            return 0

        return right - left + 1