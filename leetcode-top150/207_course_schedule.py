from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create adjacency list
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        # visited: recording the current DFS path
        visited = set()
        def dfs_valid(crs):
            if crs in visited: # Re-visited -> cycle 
                return False
            if graph[crs] == []: # No prerequisites -> Can be completed
                return True

            visited.add(crs)

            for pre in graph[crs]:
                if not dfs_valid(pre):
                    return False
                
            # Confirm no cycle for the path of this course
            visited.remove(crs)
            graph[crs] = [] # avoid re-checking validated prerequisites

            return True

        # Running dfs like this because graph may not be fully connected: 1 -> 2, 3 -> 4
        for crs in range(numCourses):
            if not dfs_valid(crs):
                return False
        return True

# Medium, Graph DFS
# Time: O(V+E)
# Space: O(V)