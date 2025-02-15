class Solution:
    def frequencySort(self, s: str) -> str:
        
        counter = Counter(s)
        
        ret = ""
        for c, freq in counter.most_common():
            ret += c * freq

        return ret
    
# Medium
# Sort + Hashmap
# Time: O(n log n)
# Space: O(n)

class Solution:
    def frequencySort(self, s: str) -> str:
        
        counter = Counter(s)
        max_freq = max(counter.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for char, freq in counter.items():
            buckets[freq].append(char)

        ret = ""
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                ret += c * i

        return ret
    
# Bucket sort
# Time: O(n)
# Space: O(n)