class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        return islands
    
    # Time: O(rows*cols)
    # Space: O(rows*cols) - recursion worst case 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    
                    queue = deque([(r, c)])
                    while queue:
                        x, y = queue.popleft()
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                            grid[x][y] = '0'
                            for dx, dy in directions:
                                queue.append((x + dx, y + dy))



        return islands