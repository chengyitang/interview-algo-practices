class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        seen = set()
        longest_size = float('-inf')

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest_size = max(longest_size, r - l + 1)

        return longest_size if longest_size != float('-inf') else 0

# Medium. Sliding window
# Time: O(N)
# Space: O(N)