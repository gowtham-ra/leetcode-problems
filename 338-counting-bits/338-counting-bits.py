class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for num in range(n+1):
            count = bin(num).count('1')
            ans.append(count)
        
        return ans
        
#         ans = []
        
#         for num in range(n+1):
#             ans.append(bin(num)[2:].count('1'))
        
#         return ans
            
        