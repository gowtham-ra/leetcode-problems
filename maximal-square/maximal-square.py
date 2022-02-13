class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = {}
        
        def dp(i, j):
            if i >= m or j >= n:
                return 0
            
            if (i, j) not in cache:
                right = dp(i, j+1)
                down = dp(i+1, j)
                diag = dp(i+1, j+1)
                
                cache[(i, j)] = 0
                
                if matrix[i][j] == '1':
                    cache[(i, j)] = 1 + min(right, down, diag)
            
            return cache[(i, j)]
        
        dp(0, 0)
        
        return max(cache.values()) ** 2
        