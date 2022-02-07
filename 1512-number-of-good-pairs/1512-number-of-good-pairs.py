from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = dict(Counter(nums))
        good_pairs = 0
        
        for num, count in freq.items():
            good_pairs += (count * (count-1)) // 2
        
        return good_pairs
            
        
        
        
        
        