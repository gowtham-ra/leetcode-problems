from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapp1 = dict()
        mapp2 = dict()
        
        for ch1, ch2 in zip(s, t):
            if (ch1 not in mapp1) and (ch2 not in mapp2):
                mapp1[ch1] = ch2
                mapp2[ch2] = ch1
            elif mapp1.get(ch1) != ch2 or mapp2.get(ch2) != ch1:
                return False              
        
        return True
        