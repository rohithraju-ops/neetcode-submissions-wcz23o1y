class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, a in enumerate(nums):
            comp = target - a
            if comp in seen:
                return list((seen[comp], i))
            seen[a] = i