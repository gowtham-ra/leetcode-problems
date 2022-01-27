class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = {}
        return self.climb(n)
        
    def climb(self, n):
        if n <= 2:
            return n
        
        if n not in self.cache:
            self.cache[n] = self.climb(n-1) + self.climb(n-2)
        
        return self.cache[n]
