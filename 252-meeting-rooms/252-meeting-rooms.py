class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        N = len(intervals)
        
        if N <= 1:
            return True
        
        intervals.sort(key=lambda x: x[0])        
        idx = 1
        
        for idx in range(1, N):
            if intervals[idx][0] < intervals[idx-1][1]:
                return False
        
        return True
        
        
        
        
        
        
        