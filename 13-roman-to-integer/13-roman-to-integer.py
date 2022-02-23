class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        symbols = ['I', 'V', 'X', 'L', ]
        values = []
        prev = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
        
        
        for i, ch in enumerate(s):
            if i > 0 and ch != 'I' and s[i-1] == prev[ch]: 
                    val1 = values.pop()
                    values.append(mapp[ch]-val1)
            else:
                values.append(mapp[ch])
            
        
        return sum(values)
                
                
                
                    
                
        