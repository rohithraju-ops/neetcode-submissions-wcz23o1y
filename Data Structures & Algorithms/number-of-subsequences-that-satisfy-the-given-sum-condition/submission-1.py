class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        r = len(nums) - 1
        mod = (10**9) + 7

        for i, left in enumerate(nums):
            while i <= r and (left + nums[r]) > target :
                r -= 1
            if i <= r:
                res += (2 ** (r - i))
                res %= mod

        return res