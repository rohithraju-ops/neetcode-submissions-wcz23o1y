class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k) - self.atmost(nums,k-1)
    
    def atmost(self, nums, k):
        from collections import defaultdict
        l = 0 
        count = 0
        maps = defaultdict(int)
        for r in range(len(nums)):
            maps[nums[r]] += 1
            
            while len(maps) > k :
                maps[nums[l]] -= 1
                if maps[nums[l]] == 0:
                    del maps[nums[l]]
                l += 1
            count += r - l + 1
        return count

        