class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows = cols = n
        matrix = [[0]*rows for i in range(cols) ]
        from math import ceil
        # a function to complete the row/col with direction
        def complete(r,c, dr, dc):
            nr, nc = r+ dr, c+dc
            prev = matrix[r][c] # already filles
            while (nr>=0 and nc>=0 and nr<rows and nc <cols and matrix[nr][nc]==0):
                matrix[nr][nc] = prev+1
                prev+=1
                nr+=dr
                nc+=dc 
            return nr-dr,nc-dc
        
        r,c =0,0
        matrix[r][c]=1

        for i in range(ceil(n/2)):
            r,c = complete(r,c, 0, 1) # right
            r,c = complete(r,c, 1, 0 ) # down
            r,c = complete(r,c, 0, -1) # left
            r,c = complete(r,c, -1, 0) # up

        return matrix