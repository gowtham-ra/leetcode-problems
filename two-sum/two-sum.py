from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = defaultdict(int)
        
        for idx, num in enumerate(nums):
            if num in mapp:
                return [mapp[num], idx]
            mapp[target-num] = idx
        
        
        
        
        