"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = {} # use a map to save copy
        queue = deque([node])

        # Copy starting node
        visited[node] = Node(node.val) 

        while queue:
            cur_node = queue.popleft()

            # Loop through current node's neighbors
            for nei in cur_node.neighbors:
                if nei not in visited:
                    # Copy the neighbor and add to visited
                    visited[nei] = Node(nei.val)
                    queue.append(nei)

                visited[cur_node].neighbors.append(visited[nei])

        return visited[node]
        
# Medium, BFS approach
# Time: O(V+E)
# Space: O(V)