class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 1 # first element must be kept
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]: # new unique number
                nums[l] = nums[i]
                l += 1
        return l
        
# Easy.
# Array
# Time: O(n)
# Space: O(1)