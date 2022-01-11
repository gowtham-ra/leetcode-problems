class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.M = len(grid)
        self.N = len(grid[0])
        starts = []
        islands = 0
        
        self.visited = [[False for _ in range(self.N)] for _ in range(self.M)]
        self.x = [-1, 1, 0, 0] 
        self.y = [0, 0, -1, 1]
        
        
        for r in range(self.M):
            for c in range(self.N):
                if grid[r][c] == '1':
                    starts.append((r, c))
        
        while starts:
            r, c = starts.pop()                        
            if not self.visited[r][c]:
                islands += 1
                self.dfs(r, c, grid)
        
        return islands
    
    def dfs(self, r, c, grid):
        self.visited[r][c] = True
        
        for i in range(4):
            row = r + self.x[i]
            col = c + self.y[i]
            
            if self.validCell(row, col) and not self.visited[row][col] and grid[row][col] == '1':
                self.dfs(row, col, grid)
    
    def validCell(self, r, c):
        return r >= 0 and r < self.M and c >= 0 and c < self.N
                
                
        
        
        
                
                
                    
        