class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols= len(matrix), len(matrix[0])
        row_zero= set()
        col_zero= set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    row_zero.add(r)
                    col_zero.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in row_zero or c in col_zero:
                    matrix[r][c]=0
            

        