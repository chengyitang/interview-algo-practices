class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        cur_max = float('-inf')

        while l < r:
            volume = (r - l) * min(height[l], height[r])
            cur_max = max(cur_max, volume)

            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1

        return cur_max
            

# Medium (easy).
# Two pointers
# Time: O(N)
# Space: O(1)