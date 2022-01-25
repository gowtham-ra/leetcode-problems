class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        req_sum = n * (n+1) // 2
        act_sum = sum(nums)
        
        return req_sum - act_sum
        