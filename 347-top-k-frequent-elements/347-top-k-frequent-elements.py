from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict(Counter(nums))
        max_heap = []
        heapq.heapify(max_heap)
        
        for key, val in frequency.items():
            heapq.heappush(max_heap, (-val, key))
        
        answer = []
        while k > 0:
            val, key = heapq.heappop(max_heap)
            answer.append(key)
            k -= 1
        
        return answer
            
        
        