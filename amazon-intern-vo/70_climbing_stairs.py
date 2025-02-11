class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

        # Time: O(N)
        # Space: O(N) -> can further use concept of fibonacci number to get rid of extra space usage
        # 509. Fibonacci Number (same concept)