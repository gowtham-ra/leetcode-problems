from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                set1 = set()
                set2 = set()
                queue = deque()
                queue.append(i)
                set1.add(i)


                while queue:
                    u = queue.popleft()
                    visited[u] = True

                    if u in set1:
                        add = set2
                        other = set1
                    else:
                        add = set1
                        other = set2

                    for v in graph[u]:
                        if not visited[v]:
                            if v not in other:
                                add.add(v)
                                queue.append(v)
                            else:
                                return False

        return True







