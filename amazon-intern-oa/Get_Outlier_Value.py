class Solution:
    def getOutlierValue(self, arr: list[int]) -> int:

        first_max = max(arr)
        arr.remove(first_max)

        second_max = max(arr)
        arr.remove(second_max)

        if first_max != sum(arr):
            return first_max
        return second_max
    
# Test
solution = Solution()

# case 1
arr = [4, 1, 3, 16, 2, 10]
output = 16
print(solution.getOutlierValue(arr) == output)