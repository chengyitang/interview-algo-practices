# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:

            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1: # last -> right most
                    result.append(node.val)
                
                # add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
    
# Medium, variation of tree BFS, solved within one minute

# Time: O(N)
# Space: O(N)