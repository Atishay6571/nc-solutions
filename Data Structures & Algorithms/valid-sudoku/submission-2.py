class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        squares=defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                element=board[r][c]
                square=(r//3,c//3)
                if element not in rows[r]:
                    if element!=".":
                        rows[r].add(element)
                else:
                    return False
                if element not in cols[c]:
                    if element!=".":
                        cols[c].add(element)
                else:
                    return False
                if element not in squares[square]:
                    if element!=".":
                        squares[square].add(element)
                else:
                    return False
        return True