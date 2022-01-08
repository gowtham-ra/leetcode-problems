class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        inf = float('inf')
        A = [-inf] + nums + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + nums + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         N = len(nums)
#         s1, s2, s3, s4 = [], [], [], []
#         next_smaller, prev_smaller = [-1] * N, [-1] * N
#         next_greater, prev_greater = [-1] * N, [-1] * N
        
#         for i in range(N):
#             while s1 and nums[s1[-1]] > nums[i]:
#                 idx = s1.pop()
#                 next_smaller[idx] = i - idx - 1
#             s1.append(i)
                
#         for i in range(N-1, -1, -1):
#             while s2 and nums[s2[-1]] >= nums[i]:
#                 idx = s2.pop()
#                 prev_smaller[idx] = idx - i - 1
#             s2.append(i)       
        
#         for i in range(N):
#             while s3 and nums[s3[-1]] < nums[i]:
#                 idx = s3.pop()
#                 next_greater[idx] = i - idx - 1
#             s3.append(i)
                
#         for i in range(N-1, -1, -1):
#             while s4 and nums[s4[-1]] <= nums[i]:
#                 idx = s4.pop()
#                 prev_greater[idx] = idx - i - 1
#             s2.append(i)  
        
#         min_ans = 0
#         max_ans = 0
#         for i in range(N):
#             min_ans += (nums[i] * (next_smaller[i]+1) * (prev_smaller[i]+1))
#             max_ans += (nums[i] * (next_greater[i]+1) * (prev_greater[i]+1))
        
#         return (max_ans-min_ans)