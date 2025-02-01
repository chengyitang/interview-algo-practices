from typing import List

def compactList(inputListSize: int, inputList: List[int]) -> List[str]:

    if not inputList:
        return []
    
    def format_interval(start, end):
        return f"{start} to {end}" if start != end else str(start)
    
    result = []
    start = inputList[0]
    prev = start

    for i in range(1, inputListSize):
        if inputList[i] != prev + 1: # new interval
            result.append(format_interval(start, prev))
            start = inputList[i] # update start
        prev = inputList[i]

    # for last interval
    result.append(format_interval(start, prev))
    return result

#print(compactList(8, [1, 2, 3, 6, 7, 8, 10, 15]))
assert(compactList(8, [1, 2, 3, 6, 7, 8, 10, 15]) == ["1 to 3", "6 to 8", "10", "15"] )