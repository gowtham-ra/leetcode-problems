from collections import deque, defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u1, v1, u2, v2 = (0, 0, 0, 0)
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        
        if u1 == u2 or u1 == v2:
            return u1
        else:
            return v1
        
        
            
            
#         adj = defaultdict(list)
        
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)
        
#         N = len(adj.keys())
#         start = 1
#         queue = deque()
#         queue.append(start)
        
#         while len(queue) > 0:
#             u = queue.pop()
        
        