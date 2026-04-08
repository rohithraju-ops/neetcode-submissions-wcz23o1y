class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cap = 2*len(nums)
        ans = [0]*cap
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans