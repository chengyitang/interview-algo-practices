class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return []

        d = defaultdict(list)

        for s in strs:
            root_anagram = ''.join(sorted(s))
            d[root_anagram].append(s)

        return list(d.values())
    
# Easy-Medium
# Time: O(N * KlogK)
# Space: O(NK)