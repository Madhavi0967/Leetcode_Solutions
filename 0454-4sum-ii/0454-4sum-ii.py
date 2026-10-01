class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count = {}
        for a in nums1:
            for b in nums2:
                s = a + b
                count[s] = count.get(s, 0) + 1

        total = 0
        for c in nums3:
            for d in nums4:
                total += count.get(-(c + d), 0)

        return total