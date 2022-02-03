class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = [nums[0]]
        
        for i in range(1, len(nums)):
            val = run_sum[-1] + nums[i]
            run_sum.append(val)
        
        return run_sum