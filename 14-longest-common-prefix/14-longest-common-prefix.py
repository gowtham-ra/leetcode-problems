class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlength = float('inf')
        prefix = ""
        done = False
        
        for word in strs:
            minlength = min(minlength, len(word))
            
        for idx in range(minlength):
            for i in range(len(strs)-1):
                if strs[i][idx] != strs[i+1][idx]:
                    done = True
                    break
            else:
                prefix += strs[0][idx]
            
            if done:
                break
        
        return prefix
        
        