class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        def ways(i, j):
            if i == 0 or j == 0:
                return 1
            
            if dp[i][j] == -1:
                dp[i][j] = ways(i-1, j) + ways(i, j-1)
            
            return dp[i][j]
        
        return ways(m-1, n-1)
            
            
        