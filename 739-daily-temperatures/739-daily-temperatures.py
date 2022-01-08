class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = len(temperatures)
        answer = [0] * days
        stack = []
        
        for cur_day, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                prev_day = stack.pop()
                diff = cur_day - prev_day
                answer[prev_day] = diff
            
            stack.append(cur_day)
        
        return answer
                
                
            
        
        