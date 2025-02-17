class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        """
        ["training", "trainer", "train"]
        longest common prefix string = "train"

        ["abc", "def", "ghi"]
        return ""


        LCP = "training"
        go through all chars in trainer:
        'e' - > "train"
        """

        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1] # remove last
                if prefix == "":
                    return ""
        return prefix

# Easy.
# String
# Time: O(n)
# Space: O(1)