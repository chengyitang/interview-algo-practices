class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # TO-DO: check null

        d = defaultdict(list)

        for s in strs: # O(n)
            root_anagram = ''.join(sorted(s)) # O(klogk)
            d[root_anagram].append(s) # O(1)

        return list(d.values())

# Medium. Hashmap. Sorting.
# Time: O(n * klogk)
# Space: O(n * k)

# Categorize by Count
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list) # (tuple, list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            d[tuple(count)].append(s)

        return list(d.values())
    
# Time: O(n * k)
# Space: O(n * k)
# 確保所有字母都為小寫才能使用
