class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = set()
        
        for num in nums:
            if num not in answer:
                answer.add(num)
            else:
                answer.remove(num)
        
        return next(iter(answer))
        
        
        