class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        r = 0
        c = N-1
        
        if M == 1 and N == 1:
            return target == matrix[0][0]
      
        while r < M and c >= 0:
            cur_val = matrix[r][c]
            if cur_val == target:
                return True
            elif target > cur_val:
                r += 1
            else:
                c -= 1
        
        return False
                
        
        
            
            
            
            
        