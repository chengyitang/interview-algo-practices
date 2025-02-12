class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # greedy, one pass
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        return total_profit
    
# Medium (Easy)
# Time: O(n)
# Space: O(1)
