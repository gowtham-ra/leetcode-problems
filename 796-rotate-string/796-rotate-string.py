class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N = len(s)
        
        for i in range(N):
            new_word = s[1:]  + s[0]
            s = new_word
            
            if new_word == goal:
                return True
        
        return False
        
        