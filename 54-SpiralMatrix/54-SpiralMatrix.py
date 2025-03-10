from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])
        left, top = 0, 0
        bottom, right = rows - 1, cols - 1

        while left <= right and top <= bottom:
            
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1    

            
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  

            if top <= bottom:
                
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1 

        return result
