from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for string in strs:
            sort = ''.join(sorted(string))
            grp[sort].append(string)
        return list(grp.values())

        
        