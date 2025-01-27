# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        result = []
        queue = deque([root])
        reverse = False

        while queue:

            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                # add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # append zigzagly to result
            if not reverse:
                result.append(level_values)
                reverse = True
            else:
                level_values.reverse()
                result.append(level_values)
                reverse = False

        return result
                

# Medium, variation of 102 (binary tree level order traversal), solved within 2 minutes

# Time: O(N)
# Space: O(N)