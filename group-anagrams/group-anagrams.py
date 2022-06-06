from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        mapp = defaultdict(list)
        answer = []
        
        for word in strs:
            sorted_word = str(sorted(word))
            mapp[sorted_word].append(word)
        
        answer.extend(mapp.values())
        
        return answer
            
                
        
        