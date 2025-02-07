# Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        return str(x) == str(x)[::-1]

        # Time: O(N)
        # Space: O(N)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        # if ends with 0, first digit must be zero, unless it's 0
        if x != 0 and x % 10 == 0:
            return False

        reversed_n = 0
        original = x

        while x > 0:
            digit = x % 10 # last digit of x
            reversed_n = reversed_n * 10 + digit
            x //= 10

        return original == reversed_n

        # Time: O(log x)
        # Space: O(1)

        # 5     (1-9)        -> 1次   = log₁₀(10¹)
        # 42    (10-99)      -> 2次   = log₁₀(10²)
        # 123   (100-999)    -> 3次   = log₁₀(10³)
        # 1234  (1000-9999)  -> 4次   = log₁₀(10⁴)

