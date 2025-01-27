"""leetcode 56. Merge Intervals"""

def findOverlappingTimes(intervals: list[list[int]]) -> list[list[int]]:

    # sort by start: n log n
    intervals.sort(key=lambda x: x[0])

    output = [intervals[0]] # keep track of the last end

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output

intervals = [[7, 7], [2, 3], [6, 11], [1, 2]]
output = [[1, 3], [6, 11]]

print(findOverlappingTimes(intervals) == output)