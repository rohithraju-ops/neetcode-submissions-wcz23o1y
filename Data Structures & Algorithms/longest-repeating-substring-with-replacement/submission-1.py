class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = 0
        max_len = 0
        nos = {}

        for right in range(len(s)):

            nos[s[right]] = nos.get(s[right], 0) + 1
            max_freq = max( max_freq, nos[s[right]])

            while (right - left + 1) -  max_freq > k:
                nos[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len

        