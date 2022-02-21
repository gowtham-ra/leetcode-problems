from collections import Counter

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0
        
        for word in words:
            if self.stretchy(s, word):
                count += 1
        
        return count
    
    def stretchy(self, word1, word2):
        i, j = 0, 0
        m, n = len(word1), len(word2)
        
        while i < m and j < n:
            if word1[i] == word2[j]:
                len1 = self.getLength(word1, i)
                len2 = self.getLength(word2, j)
                
                if (len1<3 and len1!=len2) or (len1 >= 3 and len1 < len2):
                    return False
                
                i += len1
                j += len2
                
            else:
                return False
        
        return i == m and j == n
    
    def getLength(self, word, idx):
        ch = word[idx]
        i = idx
        
        while i < len(word):
            if word[i] == ch:
                i += 1
            else:
                break
        
        return i - idx
        
        