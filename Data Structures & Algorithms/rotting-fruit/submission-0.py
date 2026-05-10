class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # store initial rotten fruit

        rows = len(grid)
        cols = len(grid[0])
        numfresh = 0
        q = deque()
        # q: (0,0),(0,1),(1,1),(1,2),(2,1),(2,2)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    numfresh+=1
        
        if numfresh == 0: return 0
        
        t=0
        dirn = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            if numfresh == 0: break
            t+=1
            for _ in range(len(q)):
                row,col = q.popleft()
                for x, y in dirn:
                    nr = row+x
                    nc = col+y
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        numfresh-=1
        if numfresh == 0:
            return t 
        else :
            return -1