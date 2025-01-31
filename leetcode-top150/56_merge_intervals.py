class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
        
        # sort by interval start values
        intervals.sort(key=lambda x: x[0])

        output = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end: # cur start <= prev end then merge
                end = max(end, intervals[i][1]) # update temp interval end (with the larger one!)
            else: # close interval
                output.append([start, end])
                start, end = intervals[i]

        # for the last interval
        output.append([start, end])

        return output
    
# Medium
# Remember the lambda usage
# Time: O(NlogN)
# Space: O(N)