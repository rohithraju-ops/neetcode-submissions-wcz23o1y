class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        lmax = height[l]
        rmax = height[r]
        area = 0
        while l <= r:
            if lmax < rmax:
                lmax = max(lmax, height[l])
                area += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                area += rmax - height[r]
                r -= 1
        return area 



        