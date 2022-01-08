class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        s1, s2 = [], []
        next_smaller, prev_smaller = [0] * N, [0] * N
        
        for i in range(N):
            next_smaller[i] = N - i - 1
            prev_smaller[i] = i
        
        for i in range(N):
            while s1 and arr[s1[-1]] > arr[i]:
                idx = s1.pop()
                next_smaller[idx] = i - idx - 1
            s1.append(i)
                
        for i in range(N-1, -1, -1):
            while s2 and arr[s2[-1]] >= arr[i]:
                idx = s2.pop()
                prev_smaller[idx] = idx - i - 1
            s2.append(i)
        
        summ = 0
        mod = 1000000007
        
        for i in range(N):
            summ += arr[i] * (next_smaller[i]+1) * (prev_smaller[i]+1) % mod
        
        return summ % mod
        
            
        
        