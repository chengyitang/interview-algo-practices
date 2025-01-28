# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.min_diff = float('inf')
        self.prev = None

        # inorder -> ascending order list
        def inorder_dfs(node):

            if not node:
                return 

            # inorder implementation
            inorder_dfs(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev.val))
            self.prev = node

            inorder_dfs(node.right)

        inorder_dfs(root)
        return self.min_diff
    
# Easy, but DFS is not as straight forward as BFS for me. Need more practice.
        
# Time: O(N)
# Space: O(N) for recursion stack
