class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0

        # sort by ends
        points.sort(key=lambda x: x[1])

        shots = 1
        curr_end = points[0][1] 

        # only need to track if the next interval's start is still inside first interval's range
        for start, end in points[1:]:
            if start > curr_end:
                shots += 1
                curr_end = end

        return shots
    
# Medium
# Time: O(NlogN)
# Space: O(1)