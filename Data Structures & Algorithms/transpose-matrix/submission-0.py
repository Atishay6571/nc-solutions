class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,cols= len(matrix), len(matrix[0])
        result = [ [0] * rows for i in range(cols)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                result[c][r]= matrix[r][c]
        return result
