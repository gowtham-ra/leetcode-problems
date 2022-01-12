class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binsearch(nums, target, 0, len(nums)-1)
        
    def binsearch(self, nums, target, start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binsearch(nums, target, mid+1, end)
        else:
            return self.binsearch(nums, target, start, mid-1)
    
    
        