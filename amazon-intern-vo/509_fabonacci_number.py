class Solution:
    def fib(self, n: int) -> int:
        
        first = 0
        second = 1
        third = 0

        if n < 2:
            return n

        for i in range(2, n + 1):
            third = first + second
            first = second
            second = third

        return third

        # Time: O(N)
        # Space: O(1)
        # 70. Climbing Stairs (same concept)