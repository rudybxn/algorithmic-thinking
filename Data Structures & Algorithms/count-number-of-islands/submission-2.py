class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row,col):
            if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]=="0":
                return
            
            grid[row][col] = "0"
            dirn = ((1,0),(0,1),(-1,0), (0,-1))
            for x, y in dirn:
                nrow = x+row
                ncol = y+col
                dfs(nrow,ncol)
            return 
        ctr = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    ctr+=1
        return ctr
        
