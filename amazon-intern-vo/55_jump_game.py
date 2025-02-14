class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # greedy
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0 # check if can reach to end from start
    
# Medium
# Array, Greedy, (DP)
# Time: O(n)
# Space: O(1)