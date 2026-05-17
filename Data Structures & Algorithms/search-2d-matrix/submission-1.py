class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row -1
            else :
                break
        else:
            return False 
        
        left, right = 0, len(matrix[row]) - 1

        while left <= right:
            mid = (left + right)//2
            if target == matrix[row][mid]:
                return True 
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1 
        else:
            return False
        