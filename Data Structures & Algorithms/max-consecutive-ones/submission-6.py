class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counts = 0
        counts = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counts += 1
                max_counts = max(max_counts, counts)
            else:
                counts = 0
        return max_counts
        
        