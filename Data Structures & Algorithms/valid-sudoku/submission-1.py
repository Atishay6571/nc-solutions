class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for row in board:
            visit=set()
            for i in row:
                if i in visit:
                    return False
                if i==".":
                    continue
                visit.add(i)
        col=defaultdict(list)
        #col check
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in col[c]:
                    return False
                if board[r][c]==".":
                    continue
                col[c].append(board[r][c])
        #box check
        for i in range(3):
            for j in range(3):
                ans=self.box(i*3,j*3,board)
                if ans==False:
                    return ans
        return True        
    def box(self,r,c,board):
        points=set()
        for i in range(3):
            for j in range(3):
                if board[r+i][c+j] in points:
                    return False
                if board[r+i][c+j]==".":
                    continue
                points.add(board[r+i][c+j])
        return True
        


        

        
            
        

