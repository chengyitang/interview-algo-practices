class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # [rob1, rob2, n, n+1, ...]
        rob1, rob2 = 0, 0
        for n in nums:
            curAmount = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = curAmount
        return rob2

        # [1, 2, 3, 1]
        
        # n == 1, curAmount = max(1 + 0, 0) = 1, rob1 = 0, rob2 = 1
        # n == 2, curAmount = max(2 + 0, 1) = 2, rob1 = 1, rob2 = 2
        # n == 3, curamount = max(3 + 1, 2) = 4, rob1 = 2, rob2 = 4
        # n == 1, curAmount = max(1 + 2 ,4) = 4, rob1 = 4, rob2 = 4

        # Time: O(n)
        # Space: O(1)