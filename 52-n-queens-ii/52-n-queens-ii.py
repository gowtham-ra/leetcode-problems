class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negDiag = set()
        posDiag = set()
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        def not_under_attack(r, c):
            return not (c in col or (r-c) in negDiag or (r+c) in posDiag)
        
        def place_queen(r, c):
            col.add(c)
            negDiag.add(r-c)
            posDiag.add(r+c)
            board[r][c] = 'Q'
        
        def remove_queen(r, c):
            col.remove(c)
            negDiag.remove(r-c)
            posDiag.remove(r+c)
            board[r][c] = '.'
        
        def backtrack(r=0, count=0):
            for c in range(n):
                if not_under_attack(r, c):
                    place_queen(r, c)
                    
                    if r == n-1:
                        count += 1
                    else:
                        count = backtrack(r+1, count)
                
                    remove_queen(r, c)
            
            return count
        
        return backtrack()
       