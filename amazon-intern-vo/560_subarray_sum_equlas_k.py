class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # find how many way that (current sum - prefix sum = k)
        # 概念：在當前的subarray中，有多少prefix sum可以等於current sum - k
            
        counts = 0
        prefixCounts = defaultdict(int)
        prefixCounts[0] += 1
        currentSum = 0

        for n in nums:
            currentSum += n
            if currentSum - k in prefixCounts:
                counts += prefixCounts[currentSum - k]
            prefixCounts[currentSum] += 1
        return counts

# Medium
# Array, Hash Table

# Time: O(n)
# Space: O(n)   