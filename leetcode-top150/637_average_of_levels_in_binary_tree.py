# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []

        # BFS
        result = []
        queue = deque([root])

        while queue:

            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_avg = float(level_sum / level_size)
            
            result.append(level_avg)

        return result
    
# Easy problem, good for reviewing BFS.

# Time: O(N)
# Space: O(N)