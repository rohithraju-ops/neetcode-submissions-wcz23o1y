class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                for element in row:
                    if target == element:
                        return True 
        
        return False 
        
        