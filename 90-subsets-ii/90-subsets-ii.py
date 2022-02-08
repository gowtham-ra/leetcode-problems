class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            n = len(subsets)
            
            for i in range(n):
                sub = subsets[i].copy()
                sub.append(num)
                sub.sort()
                if sub not in subsets:
                    subsets.append(sub)
        
        return subsets