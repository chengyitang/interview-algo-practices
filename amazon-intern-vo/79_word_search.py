# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board:
            return False

        rows, cols = len(board), len(board[0])
        visited = set() # track the path

        def dfs(r, c, i):
            # base case
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c)) # char matched, marked as visited 
                
            canFindNextWord = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))

            visited.remove((r, c)) # backtrack for mark
        
            return canFindNextWord
            

        i = 0 # word index
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, i):
                    return True
        return False
    
# Medium
# Matrix, DFS, Backtracking
# Time: O(rows * cols * 3^len(word)) # (won't go back, but explore 3 other directions)
# Space: O(len(word)) # visited set, worst case is the word is the whole board