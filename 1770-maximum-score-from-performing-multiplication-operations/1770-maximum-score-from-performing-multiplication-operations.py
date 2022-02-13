class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Bottom Up
        m = len(multipliers)
        n = len(nums)
        dp = [[0] * (m+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for l in range(i, -1, -1):
                mult = multipliers[i]
                r = (n-1) - (i-l)
                
                dp[i][l] = max(mult * nums[l] + dp[i+1][l+1],
                              mult * nums[r] + dp[i+1][l])
        
        return dp[0][0]
        
        
        
        # lru_cache from functools automatically memoizes the function
#         @lru_cache(2000)
#         def dp(i, left):
#             # Base case
#             if i == m:
#                 return 0

#             mult = multipliers[i]
#             right = n - 1 - (i - left)
            
#             # Recurrence relation
#             return max(mult * nums[left] + dp(i + 1, left + 1), 
#                        mult * nums[right] + dp(i + 1, left))
                       
#         n, m = len(nums), len(multipliers)
#         return dp(0, 0)
    
        