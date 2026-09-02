class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = 0
        ans = 100000
        l = 0
        for r in range(len(nums)) :
            sums += nums[r]
            while sums >= target:
                ans = min(ans, r - l + 1)
                sums -= nums[l]
                l += 1
        return ans if ans!= 100000 else 0
        