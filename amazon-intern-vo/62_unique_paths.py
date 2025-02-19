class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1] * n for _ in range(m)] # m = row, n = col

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp [m - 1][n - 1]                
    
# DP
# Time: O(m * n)
# Space: O(m * n)
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        return factorial(m + n - 2) // factorial(m -1) // factorial(n - 1)

# Math
# Time: O((M+N)(log(M+N)loglog(M+N)^2) 
# Space: O(1)