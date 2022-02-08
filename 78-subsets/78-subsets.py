class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            n = len(subsets)
            
            for i in range(n):
                sub = subsets[i].copy()
                sub.append(num)
                subsets.append(sub)
        
        return subsets
        