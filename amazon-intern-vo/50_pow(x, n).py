class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power: # O(logN)
            if power % 2 == 1: # if power is odd, multiply x to res
                res *= x
            x *= x # square x
            power //= 2 # divide power by 2

        return res if n >= 0 else 1 / res # if n is negative, return 1 / res    

# Medium
# Math, Recursion
# Time: O(logN)
# Space: O(1)