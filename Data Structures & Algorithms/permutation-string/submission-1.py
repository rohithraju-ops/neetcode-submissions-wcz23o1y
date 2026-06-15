from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True 

        for i in range(len(s1), len(s2)):
            # add a character on the right 
            window_count[s2[i]] += 1
            # remove the character on the left
            left_char = s2[i - len(s1)]
            window_count[left_char] -= 1

            if window_count[left_char] == 0:
                del window_count[left_char]
            
            if window_count == s1_count:
                return True 

        return False 