class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # traverse and store smallest dist from 0 cell in each non 0 and non -1 cell
                    q.append((r,c))
                    visit.add((r,c))
        
        d = 0
        dirn = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if grid[r][c]!=0:
                    grid[r][c] = d
                for x,y in dirn:
                    nr, nc =r+x,c+y
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]>0 and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        q.append((nr,nc))
            d+=1

        



        
