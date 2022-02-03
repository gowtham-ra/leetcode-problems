class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        a = intervals[0]
        
        for i in range(1, len(intervals)):
            b = intervals[i]
            
            if b[0] <= a[1]:
                a[1] = max(a[1], b[1])
            else:
                merged.append(a)
                a = b
        
        merged.append(a)
        
        return merged
        