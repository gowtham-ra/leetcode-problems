import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        big1, big2 = 0, 0
        
        while len(max_heap) >= 2:
            big1 = abs(heapq.heappop(max_heap))            
            big2 = abs(heapq.heappop(max_heap))
            
            if big1 != big2:
                heapq.heappush(max_heap, big2-big1)
        
        if max_heap:
            return abs(heapq.heappop(max_heap))
        return 0
            
        
        
        
        