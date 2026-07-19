class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        pos_diag=set()
        neg_diag=set()
        cols=set()
        board=[] #board[i] caters to columns of queen in row[i]
        def backtrack(row):
            if row == n:
                answer=[]
                for col in board:
                    eachRow=["."]*n
                    eachRow[col]="Q"
                    answer.append("".join(eachRow))
                result.append(answer)
            for col in range(n):
                if col not in cols and (row+col) not in pos_diag and (row-col) not in neg_diag:
                    # choose: place queen, add to sets
                    cols.add(col)
                    board.append(col)
                    pos_diag.add(row+col)
                    neg_diag.add(row-col)
                    # explore: backtrack(row + 1)
                    backtrack(row+1)
                    # unchoose: remove queen, remove from sets
                    cols.remove(col)
                    board.pop()
                    pos_diag.remove(row+col)
                    neg_diag.remove(row-col)
                else:
                    continue
        backtrack(0)
        return result


