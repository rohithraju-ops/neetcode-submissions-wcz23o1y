from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = defaultdict(list)
        for word in strs:
            key  = ''.join(sorted(word))
            sort[key].append(word)
        return list(sort.values())
        