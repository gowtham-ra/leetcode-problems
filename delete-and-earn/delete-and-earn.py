from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        freqMap = dict(Counter(nums))        
        nums = sorted(freqMap.keys())
        earn1, earn2 = 0, 0
        
        for i in range(len(nums)):
            curEarn = nums[i] * freqMap[nums[i]]
            
            if nums[i] == nums[i-1]+1:
                temp = earn2
                earn2 = max(earn1 + curEarn, earn2)
                earn1 = temp
            else:
                earn1, earn2 = earn2, (earn2+curEarn)
                
        
        return earn2
        
            
            
            
        
        