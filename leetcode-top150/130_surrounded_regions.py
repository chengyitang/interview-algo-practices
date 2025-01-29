class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return

        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            # exceed edge or not 'O' then return
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return

            board[r][c] = 'T' # replace 'O' with 'T', temporary

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Mark all 'O's that connects to edge
        # starts dfs from first row, last row
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == 'O':
                    dfs(r, c)

        # starts dfs from first col, last col
        for c in [0, cols - 1]:
            for r in range(rows):
                if board[r][c] == 'O':
                    dfs(r, c)

        # Replace reamining 'O's with 'X' (the surrounded regions)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

# Medium, graph dfs/bfs problem
# Time: O(rows * cols) beats 100%
# Space: O(rows * cols) - the recursion stack depth in the worst case