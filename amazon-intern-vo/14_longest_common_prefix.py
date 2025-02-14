class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # check null
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

# Easy.
# String
# Time: O(n)
# Space: O(1)