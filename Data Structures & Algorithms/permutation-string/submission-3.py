class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowCount = [0] * 26
        targetCount = [0] * 26

        windowSize = len(s1)

        if windowSize > len(s2):
            return False
        
        a = ord("a")
        for i in range(windowSize):
            targetCount[ord(s1[i]) - a] += 1
            windowCount[ord(s2[i]) - a] += 1
        
        for left in range(len(s2) - windowSize):
            if targetCount == windowCount:
                return True 
            
            right = left + windowSize

            windowCount[ord(s2[right]) - a] += 1
            windowCount[ord(s2[left]) - a] -= 1

        return targetCount == windowCount




        