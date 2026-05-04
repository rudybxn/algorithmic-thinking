class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxA = 0

        def dfs(r,c, num):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1:
                return 0
            grid[r][c]=0
            num = 1
            num+=dfs(r+1,c,num)+dfs(r-1,c,num)+dfs(r,c+1,num)+dfs(r,c-1,num)
            return num
        for r in range(rows):
            for c in range(cols):
                maxA = max(maxA, dfs(r,c,0))
        return maxA
        
                