class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def could_place_num(num, row, col):
            idx = sq_idx(row, col)
            return not (num in rows[row] or num in cols[col] or num in squares[idx])

        def place_number(num, row, col):
            rows[row].add(num)
            cols[col].add(num)
            squares[sq_idx(row, col)].add(num)
            board[row][col] = str(num)
        
        def remove_number(num, row, col):
            rows[row].remove(num)
            cols[col].remove(num)
            squares[sq_idx(row, col)].remove(num)
            board[row][col] = '.'
        
        def place_next_numbers(row, col):
            if row == N-1 and col == N-1:
                nonlocal sudoko_solved
                sudoko_solved = True
            else:
                if col == N-1:
                    backtrack(row+1, 0)
                else:
                    backtrack(row, col+1)

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for num in range(1, 10):
                    num = int(num)
                    if could_place_num(num, row, col):
                        place_number(num, row, col)
                        place_next_numbers(row, col)

                        if not sudoko_solved:
                            remove_number(num, row, col)
            else:
                place_next_numbers(row, col)

        n = 3
        N = n * n
        sq_idx = lambda row, col: (row//n) * n + (col//n)

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        squares = [set() for _ in range(9)]

        for r in range(N):
            for c in range(N):
                ch = board[r][c]              
                if ch != '.':
                    place_number(int(ch), r, c)
        
        sudoko_solved = False
        backtrack()
            
            



        
            
                        
                
                
                
        
        