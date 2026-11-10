class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total = 0

        lmax = height[0]
        rmax = height[r]

        while l < r :
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                if lmax - height[l] > 0:
                    total += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                if rmax - height[r] > 0:
                    total += rmax - height[r]
                r -= 1
        
        return total
        