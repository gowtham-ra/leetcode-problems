class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        N = len(s)
        bag = set()
        ans = 0
        
        while r < N:
            if s[r] not in bag:
                bag.add(s[r])
                r += 1
                count = r - l
                ans = max(ans, count)
            else:
                while s[r] in bag:
                    bag.remove(s[l])
                    l += 1
        
        return ans
                    
            
        