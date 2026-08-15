class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c)) # store loc of rotten

        mins = 0
        while q:
            if fresh == 0:
                break
            mins+=1
            for _ in range(len(q)):
                r,c = q.popleft()
                for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
                    newr = r+x
                    newc = c+y
                    if newr<0 or newc<0 or newr>=rows or newc>=cols or grid[newr][newc] !=1:
                        continue
                    else:
                        grid[newr][newc] = 2
                        q.append((newr,newc))
                        fresh -=1
        
        if fresh == 0:
            return mins
        else:
            return -1

                        






        
