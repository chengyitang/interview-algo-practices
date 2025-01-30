class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        order = []
        
        # Create preMap
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        # A course has 3 possible states:
        # visited: crs added to order (output)
        # visiting: crs not added to order (output), but added to cycle (dfs path)
        # unvisited: crs not added to order (output) or cycle (dfs path)
        
        cycle = set() # Track the current DFS path
        visited = set() # Save the visited nodes
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited: # No need to dfs visit twice
                return True

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visited.add(crs)
            order.append(crs)
            return True

        # go through all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return [] # can not finish all courses, return empty array
        return order

# Medium, Topology Sort (answer not unique). Extension of 207.
# Time: O(V+E)
# Space: O(V)