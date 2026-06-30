class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # approach: store set or dict of each row and col, will be 9 for each as 
        # boards can be 9&9 only.
        # there are 9 grids, each can be represented as (1,1),(1,2) etc in the form of 
        # (r//3, c//3) as keys for a dict.

        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r]:
                    return False
                else:
                    rows[r].add(board[r][c])
                if board[r][c] in cols[c]:
                    return False
                else:
                    cols[c].add(board[r][c])
                if board[r][c] in grids[(r//3,c//3)]:
                    return False
                else:
                    grids[(r//3,c//3)].add(board[r][c])

        return True