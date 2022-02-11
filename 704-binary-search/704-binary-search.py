class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binsearch(left, right):
            if left > right:
                return -1
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binsearch(mid+1, right)
            
            return binsearch(left, mid-1)
        
        return binsearch(0, len(nums)-1)
        
        
        
        
        
#         return self.binsearch(nums, target, 0, len(nums)-1)
        
#     def binsearch(self, nums, target, start, end):
#         if start > end:
#             return -1
        
#         mid = (start + end) // 2
        
#         if nums[mid] == target:
#             return mid
#         elif target > nums[mid]:
#             return self.binsearch(nums, target, mid+1, end)
#         else:
#             return self.binsearch(nums, target, start, mid-1)
    
    
        