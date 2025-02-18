class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        red -> white -> blue
        0       1       2

        one-pass, without sorting
        """

        l = cur = 0
        r = len(nums) - 1

        while cur <= r:
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
                # do not increment cur here: 
            else:
                cur += 1

# Medium
# two-pointer, one-pass
# Time: O(n)
# Space: O(1)

        