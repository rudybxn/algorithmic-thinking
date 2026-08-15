class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        nums = 0
        def traverse(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0":
                return 
            grid[r][c] = "0" # visited
            traverse(r+1,c)
            traverse(r-1,c)
            traverse(r,c+1)
            traverse(r,c-1)

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    nums+=1
                    traverse(r,c)

        return nums
    