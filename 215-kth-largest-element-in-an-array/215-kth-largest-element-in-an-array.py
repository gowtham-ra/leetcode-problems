from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        
        
        
            
            
        
        