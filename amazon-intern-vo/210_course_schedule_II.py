class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        order = []

        # create prerequisites graph
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        # a course has 3 states;
        # visited -> course completed
        # visiting -> course is in current path
        # not visited -> course not in current path
        visiting = set()
        visited = set()

        def valid(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)

            for pre in graph[crs]:
                if not valid(pre):
                    return False
            
            visiting.remove(crs)
            
            # course can be completed
            visited.add(crs)
            order.append(crs)
            return True
        
        for crs in range(numCourses):
            if not valid(crs):
                return []
        return order
    
# Medium
# Graph, DFS, Topological Sort  
# Time: O(V + E) = O(numCourses + len(prerequisites))
# Space: O(V) = O(numCourses) - for path set / recursion stack