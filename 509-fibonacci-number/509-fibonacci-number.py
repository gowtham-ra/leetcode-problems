class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * (n+1)
        
        def fibo(n):
            if n <= 1:
                return n
            
            if memo[n] == -1:
                memo[n] = fibo(n-1) + fibo(n-2)
            
            return memo[n]
        
        return fibo(n)