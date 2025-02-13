class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        d = {}

        # build element: next greater element map
        for num in nums2:
            while stack and num > stack[-1]:
                d[stack.pop()] = num
            stack.append(num)

        while stack:
            d[stack.pop()] = -1

        return [d[num] for num in nums1]
            
# Easy.
# Monotonic Stack
# Time: O(len(nums1) + len(nums2))
# Space: O(len(nums2))

