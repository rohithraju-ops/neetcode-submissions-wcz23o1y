class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zero_count = 0
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                zero_count += 1
            if zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
        return r - l + 1
        