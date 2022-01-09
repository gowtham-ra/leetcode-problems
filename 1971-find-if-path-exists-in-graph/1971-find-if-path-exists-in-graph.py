from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        self.graph = defaultdict(list)
        
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        self.visited = [False] * n
        self.answer = False
        self.dfs(start, end)
        return self.answer
    
        
        
    def dfs(self, cur, end):
        self.visited[cur] = True
        
        if cur == end:
            self.answer = True
                    
        if not self.answer:
            for v in self.graph[cur]:
                if not self.visited[v]:
                    self.dfs(v, end)
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         graph = defaultdict(list)
        
#         for edge in edges:
#             u1, v1 = edge
#             v2, u2 = edge
#             graph[u1].append(v1)
#             graph[u2].append(v2)
        
#         visited = [False] * n
        
#         queue = deque()
#         queue.append(start)
#         visited[start] = True
        
#         while len(queue) > 0:
#             u = queue.popleft()
            
#             if u == end:
#                 return True
            
#             for v in graph[u]:
#                 if not visited[v]:
#                     queue.append(v)
#                     visited[v] = True
        
#         return False
        
        
        
#         def dfs(curr, end):
#             nonlocal answer
#             visited[curr] = True
            
#             if curr == end:
#                 answer = True
#                 return answer
            
#             if not answer:
#                 for v in graph[curr]:

#                     if not visited[v]:
#                         dfs(v, end)

#             return answer
        
#         return dfs(start, end)
                
        