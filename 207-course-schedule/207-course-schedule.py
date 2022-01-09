from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        self.checked = [False] * numCourses
        self.visited = [False] * numCourses
        
        for v, u in prerequisites:
            graph[u].append(v) 
        
        for course in range(numCourses):
            if self.isCyclic(course, graph):
                return False
        return True
        
                
        
    def isCyclic(self, cur, graph):
        if self.checked[cur]:
            return False
        
        if self.visited[cur]:
            return True

        self.visited[cur] = True
        ret = False
        for v in graph[cur]:
            ret = self.isCyclic(v, graph)
            
            if ret: break
        
        self.visited[cur] = False
        self.checked[cur] = True
        
        return ret


            
            
        
        
#         while queue:
#             u = queue.popleft()
#             visited[u] = True
            
#             for v in graph[u]:
#                 if not visited[v] and indegrees[v]-1 >= 0:
#                     indegrees[v] -= 1
#                     queue.append(v)
#                 else:
#                     return False
        
#          return True
                    

                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        