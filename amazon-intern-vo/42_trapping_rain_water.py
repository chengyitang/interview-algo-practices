class Solution:
    def trap(self, height: List[int]) -> int:
        
        """
        trap: left >= i and i <= right
        volume = min(left_max, right_max) - height[i]
        """

        l, r = 0, len(height) - 1
        volume = 0
        left_max, right_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                volume += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                volume += right_max - height[r]
                r -= 1
        return volume

        # Hard
        # Two pointers
        # O(n)
        # O(1)