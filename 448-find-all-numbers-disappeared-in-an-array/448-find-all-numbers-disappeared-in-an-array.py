class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = {num for num in range(1, len(nums)+1)}
        
        for num in nums:
            if num in numbers:
                numbers.remove(num)
        
        return numbers
        