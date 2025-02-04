class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False
        
        pattern_d = {}
        str_d = {}

        for c, word in zip(pattern, words):
            if c in pattern_d and pattern_d[c] != word:
                return False
            if word in str_d and str_d[word] != c:
                return False
            
            pattern_d[c] = word
            str_d[word] = c

        return True
    
# Easy. Same as 205 isomorphic strings

# Time: O(N)
# Space: O(N)