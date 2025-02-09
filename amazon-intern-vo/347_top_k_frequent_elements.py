import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums) # O(n)

        max_heap = []
        for num, count in counter.items(): # O(n log n) 
            heapq.heappush(max_heap, (-count, num)) # O(log n)  

        output = []
        for _ in range(k): # O(k log n) 
            _, num = heapq.heappop(max_heap) # O(log n)
            output.append(num)

        return output
    
# Medium. Heap
# Time: O(n log n)
# Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        output = []
        for i in range(len(buckets) - 1, 0, -1): # don't have to include 0, since 0 means never seen
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
                
        return output
    
# Medium. Bucket Sort
# Time: O(n)
# Space: O(n)