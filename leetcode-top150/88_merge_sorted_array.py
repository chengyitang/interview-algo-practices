class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # ascending order

        # Fill backward
        # nums1 = [1, 2, 3, 0, 0, 0] nums2 = [2, 5, 6]
        #                p1       p                 p2

        p1, p2 = m - 1, n - 1

        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]: # ensure p1 is not out of bounds (nums2 remaining)
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

        # Time: O(n + m)
        # Space: O(1)