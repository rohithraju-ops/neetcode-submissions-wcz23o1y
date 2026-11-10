class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for i, a in enumerate(nums):
            if a > 0 :
                break

            if i == 0 or nums[i] != nums[i-1]:
                twoSum2(nums, i, result)

        return result


def twoSum2(nums, i, result):
    l = i + 1
    r = len(nums) - 1

    while l < r:
        target = nums[i] + nums[l] + nums[r]

        if target < 0 :
            l += 1
        
        elif target > 0:
            r -= 1

        else:
            result.append([ nums[i], nums[l], nums[r] ])
            l += 1
            r -= 1
            

            while l < r and nums[l] == nums[l - 1]:
                l += 1

    return result
        