class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Two pointers, one-way solution
        replace_idx = 0
        for i in range(len(nums)):
            if nums[i] != val: # no need to remove, use it for replace
                nums[replace_idx] = nums[i]
                replace_idx += 1
        return replace_idx
        
        # Time: O(n)
        # Space: O(1)