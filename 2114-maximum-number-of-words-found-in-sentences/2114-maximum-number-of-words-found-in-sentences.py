class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = 0
        
        for sentence in sentences:
            length = len(sentence.split())
            most = max(most, length)
        
        return most
        