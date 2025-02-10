class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        output = ""
        longest = 0

        for i in range(len(s)):
            # odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    output = s[l : r + 1]
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    output = s[l : r + 1]
                l -= 1
                r += 1

        return output

# Medium. Two pointers. 
# Time: O(n^2)
# Space: O(1)
# Approach: Expand from center. 注意奇数和偶数長度差異
# 感覺可以先從 Check all substring O(n^3)開始講，就不用講到 Manacher's Algorithm

# Manacher's Algorithm: O(n)