from functools import reduce

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        max_length = len(reduce(lambda x, y : x if len(x) > len(y) else y, strs))
        i = 0
        
        while i < max_length:            
            for j in range(len(strs)-1):
                if i == len(strs[j]) or i == len(strs[j+1]):
                    return output
                
                if strs[j][i] != strs[j+1][i]:
                    return output
            
            output += strs[0][i]
            i += 1
        
        return output
        
        