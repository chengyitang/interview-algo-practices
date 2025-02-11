class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # find how many way that (current sum - prefix sum = k)
        
        subarray_count = 0
        d = { 0:1 } # prefix sum : count
        cur_sum = 0

        for num in nums:
            cur_sum += num
            if cur_sum - k in d:
                subarray_count += d[cur_sum - k]
            
            # update cur_sum count
            d[cur_sum] = d.get(cur_sum, 0) + 1

        return subarray_count

# Medium
# Array, Hash Table
# Time: O(n)
# Space: O(n)   