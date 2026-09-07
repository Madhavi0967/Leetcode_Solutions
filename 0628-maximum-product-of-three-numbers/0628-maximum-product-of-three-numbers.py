class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        # The maximum product could be either the product of the three largest numbers
        # or the product of the two smallest (most negative) numbers and the largest number.
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
