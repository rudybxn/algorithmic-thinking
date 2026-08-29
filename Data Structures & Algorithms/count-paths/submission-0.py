class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {} # store i,j pairs

        def recurse(i,j):
            if i>=m or j>=n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]

            # choice: down, right
            count = recurse(i+1,j) + recurse(i,j+1)
            memo[(i,j)] = count
            return count

        return recurse(0,0)

