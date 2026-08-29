class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0 
        r = n - 1
        maxarea = 0
        while l < r:
            length = min(heights[l], heights[r])
            breadth = r - l
            area = length * breadth 
            maxarea = max(maxarea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxarea

        