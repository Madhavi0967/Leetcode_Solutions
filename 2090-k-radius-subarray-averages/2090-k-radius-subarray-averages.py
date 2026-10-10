class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avgs = [-1] * n

        if k == 0:
            return nums

        size = 2 * k + 1

        if size > n:
            return avgs

        window_sum = sum(nums[:size])
        avgs[k] = window_sum // size

        for i in range(size, n):
            window_sum += nums[i]
            window_sum -= nums[i - size]

            avgs[i - k] = window_sum // size

        return avgs