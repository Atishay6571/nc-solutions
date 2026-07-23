class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c] in ['X','S']):
                return
            board[r][c]="S" # here s stands for safe
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        #traverse first and last rows
        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c)
            if board[rows-1][c]=="O":
                dfs(rows-1,c)
        #traverse first and last columns
        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][cols-1]=="O":
                dfs(r,cols-1)

        #now change all S (safe) to O and all unsafe O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="S":
                    board[r][c]='O'
                elif board[r][c]=='O':
                    board[r][c]='X'