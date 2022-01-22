from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = Counter(nums)
        
        for i, num in enumerate(nums):
            val = target - num
            
            if val in dictionary:
                idx = nums.index(val)
                
                if idx != i:
                    return [i, idx]
                
            
        