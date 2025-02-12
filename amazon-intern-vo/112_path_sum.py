# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return (self.hasPathSum(root.left, targetSum - root.val) or
        self.hasPathSum(root.right, targetSum - root.val))



# Easy.
# Tree DFS
# Time: O(n)
# Space: best case O(logn) for balanced tree, worst case O(n) for skewed tree   
# Follow up: 113. Path Sum II