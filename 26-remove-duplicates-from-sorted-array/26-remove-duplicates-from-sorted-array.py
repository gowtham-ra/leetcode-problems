class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = -1
        prev = float('-inf')
        
        for cur in nums:
            if cur != prev:
                idx += 1
                nums[idx] = cur
                prev = cur
        
        return idx + 1
            
            
        