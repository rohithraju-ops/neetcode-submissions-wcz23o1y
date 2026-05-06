class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        suffix = []
        for i in range(len(nums)):
            prefix.append(product)
            product *= nums[i]
        prods = 1
        for i in range((len(nums)) - 1 , -1, -1 ):
            suffix.append(prods)
            prods *= nums[i]
        suffix = suffix[::-1]
        return [prefix[i] * suffix[i] for i in range(len(nums))]
            
        
        