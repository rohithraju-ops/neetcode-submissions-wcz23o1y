class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or (len(s) == 0):
            return 0
        if len(s) == 1:
            return 1

        l, r = 0, 0
        ans = 0
        charAt = set()

        while r < len(s):
            c = s[r]
            while c in charAt:
                charAt.remove(s[l])
                l += 1
            
            charAt.add(c)
            ans = max(ans, (r - l + 1))
            r += 1
        
        return ans