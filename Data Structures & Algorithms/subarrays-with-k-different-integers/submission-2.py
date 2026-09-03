class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k) - self.atmost(nums, k - 1)

    def atmost(self, nums, k):
        from collections import defaultdict
        l = 0 
        mapped = defaultdict(int)
        count = 0
        for r in range(len(nums)):
            mapped[nums[r]] += 1
                
            while len(mapped) > k :
                mapped[nums[l]] -= 1
                if mapped[nums[l]] == 0:
                    del mapped[nums[l]]
                l += 1

            count += r - l + 1
        return count 

        