class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        window = set()
        window_st = 0
        count = 0
        n = len(s)
        
        if k > n:
            return count
        
        for window_end, ch in enumerate(s):
            while ch in window:
                window.remove(s[window_st])
                window_st += 1
                
            window.add(ch)
            
            if (window_end - window_st + 1) >= k:
                count += 1
        
        return count
                
        
        
        