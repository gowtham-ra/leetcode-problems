class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = local_sum = float('-inf')
        
        for num in nums:
            local_sum = max(local_sum + num, num)
            global_sum = max(local_sum, global_sum)
        
        return global_sum
        
        
        
        