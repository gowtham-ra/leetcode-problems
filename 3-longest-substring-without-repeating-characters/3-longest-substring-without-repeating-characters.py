class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        mapp = {}
        ans = 0
        beg = 0
        
        for end in range(N):
            if s[end] in mapp:
                beg = max(mapp[s[end]], beg)
            
            ans = max(ans, end-beg+1)
            mapp[s[end]] = end + 1
        
        return ans
            
            
        