class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Easy. Not worth practice lol
# Time = Space = O(N)