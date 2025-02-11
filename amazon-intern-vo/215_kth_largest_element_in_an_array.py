class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # maintain a min heap of size k
        # when next num is larger than the smallest num in the heap, replace it
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
    
# Medium
# Array, Divide and Conquer, Sorting, Heap, Quickselect
# Time: O(nlogk)
# Space: O(k)



# Quickselect



# Time: O(n)
# Space: O(1)   

