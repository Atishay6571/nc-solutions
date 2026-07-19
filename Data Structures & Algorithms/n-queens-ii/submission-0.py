class Solution:
    def totalNQueens(self, n: int) -> int:
        count=[]
        cols=set()
        pos_diag=set()
        neg_diag=set()
        def backtrack(row):
            if row==n:
                count.append(1)
                return                
            for col in range(n):
                if (col not in cols and (row+col) not in pos_diag and (row-col) not in neg_diag):
                    cols.add(col)
                    pos_diag.add(row+col)
                    neg_diag.add(row-col)
                    backtrack(row+1)
                    cols.remove(col)
                    pos_diag.remove(row+col)
                    neg_diag.remove(row-col)
                else:
                    continue
        backtrack(0)
        return len(count)