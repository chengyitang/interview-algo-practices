class Solution:
    def getScoreDifference(self, points: list[int]) -> int:

        points.sort(reverse=True)

        # p1 first
        p1 = sum([points[i] for i in range(0, len(points), 2)])
        p2 = sum([points[i] for i in range(1, len(points), 2)])

        return p1 - p2
    
# Test
solution = Solution()

# case 1
points = [4, 1, 2, 3]
output = 2
print(solution.getScoreDifference(points) == output)

# case 2
points = [4, 1, 1, 4]
output = 0
print(solution.getScoreDifference(points) == output)

# case 1
points = [1, 3, 3]
output = 1
print(solution.getScoreDifference(points) == output)