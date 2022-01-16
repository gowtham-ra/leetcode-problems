class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        
        r = M-1
        c = 0
        
        while r >= 0 and c < N:
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                r -= 1
            else:
                c += 1
        
        return False
            
        
            
            
            
            
        