class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        counts = collections.Counter(magazine)

        for c in ransomNote:
            counts[c] -= 1
            if counts[c] < 0:
                return False

        return True
    
# Easy. Hashmap. Counter
# Time: O(m+n)
# Space: O(26) -> O(1)