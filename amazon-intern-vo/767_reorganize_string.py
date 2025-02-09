# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.
import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. 計算頻率
        counter = Counter(s)
        
        # 2. 建立最大堆（用負數）
        heap = []
        for char, freq in counter.items():
            # 如果某個字符出現次數超過 (n+1)/2，無法重組
            if freq > (len(s) + 1) // 2:  # 重要！
                return ""
            heapq.heappush(heap, (-freq, char)) # time: O(log n)
        
        # 3. 重組字串
        result = []
        while len(heap) >= 2:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)
            
            result.extend([char1, char2])
            
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, char2))
        
        # 4. 處理最後一個字符
        if heap:
            freq, char = heapq.heappop(heap)
            result.append(char)
        
        return ''.join(result)
    
# Medium (hard). Heap
# Time: O(n log n)
# Space: O(n)

# 重點：
# 1. 如果某個字符出現次數超過 (n+1)/2，無法重組
# 2. 建立最大堆（用負數）
# 3. 重組字串
# 4. 處理最後一個字符

# a - a - a -     n=6 (n+1)/2 = 3.5
# a - a - a - a   n=7 (n+1)/2 = 4


