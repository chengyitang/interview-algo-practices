class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        seen = set()
        max_len = 0

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
    

# Medium. Sliding window.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Time: O(n)
# Space: O(min(m, n)) where m is the size of the charset.