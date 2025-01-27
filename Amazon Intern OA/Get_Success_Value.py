class Solution:
    def getSuccessValue(self, num_viewers: list[int], queries: list[int]) -> list[int]:

        """return the sum of top k views"""

        output = []

        # sort
        num_viewers.sort(reverse=True)

        for k in queries:
            output.append(sum(num_viewers[:k]))

        return output
    
solution = Solution()

# case 1
num_viewers = [2, 5, 6, 3, 5]
queries = [2, 3, 5]
output = [11, 16, 21]
print(solution.getSuccessValue(num_viewers, queries) == output)

# case 2
num_viewers = [7, 3, 5, 2]
queries = [1, 4]
output = [7, 17]
print(solution.getSuccessValue(num_viewers, queries) == output)