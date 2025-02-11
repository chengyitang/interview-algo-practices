class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create prerequisites graph
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        # help function: check if a course can be completed
        path = set()
        def valid(crs):
            if crs in path:
                return False
            if graph[crs] == []: # no prerequisites
                return True
            
            # add crs to current path
            path.add(crs)

            # dfs on all prerequisites
            for pre in graph[crs]:
                if not valid(pre):
                    return False
            
            # check completed, remove course  from path
            path.remove(crs)
            # already known this course can be completed, set its prerequisites to empty list to avoid revisiting
            graph[crs] = []

            return True


        # check every course can be completed
        for crs in range(numCourses):
            if not valid(crs):
                return False
        return True
    
# Medium
# Graph, DFS, Topological Sort  
# Time: O(V + E) = O(numCourses + len(prerequisites))
# Space: O(V) = O(numCourses) - for path set / recursion stack