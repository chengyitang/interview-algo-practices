class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0]) # sort by start time

        output = []

        start, end = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                output.append([start, end])
                start, end = interval
        
        # for last interval
        output.append([start, end])
        return output
    
# Medium. Array
# Time: O(nlogn)
# Space: O(n)


