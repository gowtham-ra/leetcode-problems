class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(idx):
            if idx >= len(s)//2:
                return
            
            s[idx], s[len(s)-idx-1] = s[len(s)-idx-1], s[idx]
            reverse(idx+1)
        
        reverse(0)
            
        
        