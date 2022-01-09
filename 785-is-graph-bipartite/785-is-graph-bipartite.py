from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        self.visited = [False] * N
        self.queue = deque()
        self.answer = True
        
        for i in range(N):
            if not self.visited[i] and self.answer:
                self.bfs(i, graph)
                
        return self.answer
    
    
    def bfs(self, start, graph):
        set1 = set()
        set2 = set()

        self.queue.append(start)
        set1.add(start)

        while self.queue:
            u = self.queue.popleft()
            self.visited[u] = True

            if u in set1:
                add = set2
                other = set1
            else:
                add = set1
                other = set2

            for v in graph[u]:
                if not self.visited[v]:
                    if v not in other:
                        add.add(v)
                        self.queue.append(v)
                    else:
                        self.answer = False
                        return








