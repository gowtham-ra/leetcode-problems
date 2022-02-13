class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(i, j):
            if i == -1 or j == -1:
                return 0
            
            if dp[i][j] == -1:            
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + lcs(i-1, j-1)
                else:
                    dp[i][j] = max(lcs(i-1, j), lcs(i, j-1))
            
            return dp[i][j]
        

        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]
        return lcs(m-1, n-1)
        