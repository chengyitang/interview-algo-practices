class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # subarray with min len which sum >= target
        # brute force: go through all subarray and check sum, taking O(n sq)
        # sliding window: O(n) / O(1)
        # stop adding element when sum already >= target, keep adding element if not
        
        if not nums:
            return 0

        l = 0
        cur_sum = 0
        min_size = float('inf')

        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target: # use while: may need to remove multiple times
                min_size = min(min_size, r - l + 1)
                # remove front
                cur_sum -= nums[l]
                l += 1
        return min_size if min_size != float('inf') else 0