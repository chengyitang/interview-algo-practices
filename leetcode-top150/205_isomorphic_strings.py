class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s2t = {}
        t2s = {}

        for c1, c2 in zip(s, t):
            if c1 in s2t and s2t[c1] != c2:
                return False
            if c2 in t2s and t2s[c2] != c1:
                return False

            s2t[c1] = c2
            t2s[c2] = c1

        return True
    
# Easy. Hashmap
# Time: O(len(s)) -> O(N)
# Space: O(len(s) * 2) -> O(N)