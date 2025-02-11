# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # check null
        if not root:
            return None

        ascending_list = []

        def inorder(node):

            # base case
            if not node:
                return

            # inorder
            inorder(node.left)

            ascending_list.append(node.val)

            inorder(node.right)

        inorder(root)

        return ascending_list[k - 1]

# Medium
# Tree, Depth-First Search, Inorder Traversal
# 思路： 對 BST 做 inorder traversal 會得到一個升冪的 list
# Time: O(n)
# Space: O(n)