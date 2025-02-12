# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        pathsList = []

        def dfsTree(node, remainingSum, pathNodes, pathsList) -> None:
            if not node:
                return

            # add current node to path list
            pathNodes.append(node.val)

            # check if current node is a leaf and if it equals to remaining sum, if it is, add pathNodes to pathList
            if node.val == remainingSum and not node.left and not node.right:
                pathsList.append(list(pathNodes)) # use list to deep copy the pathNodes
            else:
                dfsTree(node.left, remainingSum - node.val, pathNodes, pathsList)
                dfsTree(node.right, remainingSum - node.val, pathNodes, pathsList)
            
            # pop the node after we're done with all its substrees
            pathNodes.pop()
            
        dfsTree(root, targetSum, [], pathsList)
        return pathsList
# Medium
# Tree DFS, Backtracking
# Time: worst case n/2 leaf nodes, for each leaf we do copy operation, O(n) -> O(n^2)
# Space: O(n)