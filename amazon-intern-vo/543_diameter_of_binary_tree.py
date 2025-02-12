# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def dfs(node):

            # base case
            if not node:
                return 0

            nonlocal diameter
            
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right) # consider the path through the current node

            return max(left, right) + 1 # single branch path

        dfs(root)
        return diameter
    
# Easy (Medium)
# Tree DFS
# Time: O(n)
# Space: O(n)
# 思路： 這題是求二元樹的直徑，直徑是任意兩個節點之間最長的路徑。
# 這題的解法是使用 DFS 來求解，DFS 的過程中，我們會計算每個節點的左子樹和右子樹的高度，並且更新直徑。
# 直徑的計算方式是左子樹的高度 + 右子樹的高度。
# 因為我們是從下往上計算，所以最後的直徑就是整棵樹的直徑。