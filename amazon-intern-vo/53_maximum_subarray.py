class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = float('-inf')
        curSum = 0

        for n in nums:
            # only 2 cases for a consideration
            # 1. previous subarray is negative, so start a new subarray
            # 2. previous subarray is positive, so add current number to the previous subarray
            curSum = max(curSum, 0) 
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum
    
# Medium
# Kadane's Algorithm (https://neetcode.io/courses/advanced-algorithms/0)
# Time: O(n)
# Space: O(1)