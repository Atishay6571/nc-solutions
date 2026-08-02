class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        rows, cols = len(image), len(image[0])
        original= image[sr][sc]
        visited=set()
        def dfs(r,c):
            image[r][c]= color
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc= dr+r, dc+ c
                if (nr<0 or nc<0 or nr>= rows or nc >= cols or image[nr][nc]!= original or (nr,nc) in visited or image[nr][nc]==color):
                    continue
                dfs(nr,nc)
        dfs(sr,sc)
        return image
            