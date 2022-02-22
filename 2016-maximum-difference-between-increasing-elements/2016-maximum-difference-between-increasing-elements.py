class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        minVal = nums[0]
        maxVal = nums[0]
        
        for i in range(1, len(nums)):
            val = nums[i]
            
            if val < minVal:
                minVal = maxVal = val
            
            if val > maxVal:
                maxVal = val
                ans = max(ans, maxVal-minVal)
            
        
        return ans
                
        
        
        