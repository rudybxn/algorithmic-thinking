class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        ctr=0

        def bfs(r,c):
            q = deque([(r,c)])
            grid[r][c] = "0" # mark visit

            while q:
                row, col = q.popleft()
                dirn = ((1,0),(0,1),(-1,0),(0,-1))
                for x,y in dirn:
                    nrow = x+row
                    ncol = y+col
                    if 0<=nrow<rows and 0<=ncol<cols and grid[nrow][ncol]!="0":
                        q.append((nrow,ncol))
                        grid[nrow][ncol]="0"
            return 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    ctr+=1

        return ctr


                    
