# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_distance = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.traverse(root, start)
        return self.max_distance

    def traverse(self, node, start):
        depth = 0
        if node is None:
            return depth

        left_depth = self.traverse(node.left, start)
        right_depth = self.traverse(node.right, start)

        if node.val == start:
            self.max_depth = max(left_depth, right_depth)
            depth -= 1 # distance of root to start
        elif left_depth >= 0 and right_depth >= 0:
            depth = max(left_depth, right_depth) + 1
        else:
            distance = abs(left_depth) + abs(right_depth)
            self.max_distance = max(self.max_distance, distance)
            depth = min(left_depth, right_depth) - 1

        return depth

# Tree DFS