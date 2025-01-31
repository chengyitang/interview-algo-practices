class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
        
        # insert
        intervals.append(newInterval)

        # re-sort intervals
        intervals.sort(key=lambda x: x[0])

        # merge intervals
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
    
# Medium, just simply insert and then re-use 56's merge intervals process.
# Time: O(NlogN)
# Space: O(N)