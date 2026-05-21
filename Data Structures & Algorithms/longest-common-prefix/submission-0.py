class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        reference = strs[0]

        for i in range(len(reference)):
            char = reference[i]

            for word in strs[1:]:
                if i >= len(word) or char != word[i]:
                    return prefix
            
            prefix += char 
        
        return prefix
        