# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.ascending_list = []

        def inorder(node):

            if not node:
                return

            # inorder
            inorder(node.left)

            self.ascending_list.append(node.val)

            inorder(node.right)

        inorder(root)
        return self.ascending_list[k - 1] if self.ascending_list else None
    
# Same pattern as 530 (BST DFS - inorder)
# Medium but feel like even easier than 530 (easy)

# Time: O(N)
# Space: O(N)