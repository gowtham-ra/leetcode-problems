class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        cur_min = math.inf
        cur_ans = 0
        nums.sort()
        
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            
            while j < k:
                summ = nums[i] + nums[j] + nums[k]                
                diff = abs(summ-target)
                
                if diff < cur_min:
                    cur_min = diff
                    cur_ans = summ
                
                if summ == target:
                    return summ
                elif summ < target:
                    j += 1
                else:
                    k -= 1
            
        return cur_ans
                    
                
                
        