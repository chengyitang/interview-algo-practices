## DFS ##
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r, c):

            # possible base cases of dfs for an single island
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0' # marked as visited

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)

        return num_islands
    
# DFS solution 81.5%
# Time: O(rows * cols)
# Space: O(rows * cols) - worst case: all '1', the recursion stack depth may be rows * cols


## BFS ##
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        num_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1

                    # use bfs to explore island
                    queue = deque([(r, c)])
                    while queue:
                        x, y = queue.popleft() # cannot use 'r' and 'c' as var repeatly
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                            grid[x][y] = '0' # mark as visited
                            for dx, dy in directions:
                                queue.append((x + dx, y + dy))

        return num_islands
    
# BFS solution 52.56%
# Time: O(rows * cols)
# Space: O(rows * cols) - worst case: all '1', the recursion stack depth may be rows * cols