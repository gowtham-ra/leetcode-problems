class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        negDiag = set()
        posDiag = set()
        
        res = []
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
        
        def backtrack(r=0):
            for c in range(n):
                if not_under_attack(r, c):
                    place_queen(r, c)
                    
                    if r == n-1:
                        copy = ["".join(row) for row in board]
                        res.append(copy)
                    else:
                        backtrack(r+1)
                
                    remove_queen(r, c)
        
        backtrack()
        return res
        
        