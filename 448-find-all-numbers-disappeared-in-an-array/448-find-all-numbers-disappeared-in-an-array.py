class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # TC: O(n) and SC:O(1)
        i = 0
        
        while i < len(nums):
            idx = abs(nums[i]) - 1            
            nums[idx] = - abs(nums[idx])
            
            i += 1
        
        answer = []
        for idx, num in enumerate(nums):
            if num >  0:
                answer.append(idx+1)
        
        return answer
                
            
            
            
        
        
        
        
        
        
        # TC: O(n) and SC: O(n)
#         numbers = {num for num in range(1, len(nums)+1)}
        
#         for num in nums:
#             if num in numbers:
#                 numbers.remove(num)
        
#         return numbers
