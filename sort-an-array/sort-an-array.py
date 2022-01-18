class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
    
    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums)//2
        left = self.mergesort(nums[0:pivot])
        right = self.mergesort(nums[pivot:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        l, r = 0, 0
        result = []
        M = len(left)
        N = len(right)
        
        while l < M and r < N:
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        
        result.extend(left[l:])
        result.extend(right[r:])
        
        return result
        
        
        