class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        
        cur_interval = intervals[0]
        merged_intervals = [cur_interval]
        
        for i in range(1, len(intervals)):
            cur_start = cur_interval[0]
            cur_end = cur_interval[1]
            next_start = intervals[i][0]
            next_end = intervals[i][1]
            
            if next_start <= cur_end:
                cur_end = max(cur_end, next_end)
                merged_intervals[-1][1] = cur_end
            else:
                merged_intervals.append([next_start, next_end])
            
            cur_interval = merged_intervals[-1]
        
        return merged_intervals
            
        
        