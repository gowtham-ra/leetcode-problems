from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency_map = dict(Counter(s))
        
        for idx, ch in enumerate(s):
            if frequency_map[ch] == 1:
                return idx
        
        return -1
            
        