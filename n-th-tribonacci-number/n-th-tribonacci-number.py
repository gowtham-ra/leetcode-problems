class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(i):
            if i == 0:
                memo[i] = 0
            elif i <= 2:
                memo[i] = 1
            
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
            
            return memo[i]
        
        memo = {}
        dp(n)
        
        return memo[n]
                
        