class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        l = 0
        max_count = 0
        count = defaultdict(int)
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            max_count = max(max_count, r - l + 1)
        
        return max_count

        