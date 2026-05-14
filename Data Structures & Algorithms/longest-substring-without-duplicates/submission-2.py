class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        charset = set()
        left = 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1

            charset.add(s[right])
            max_len = max(max_len, len(charset))

        return max_len
        