from math import floor
from typing import List
from collections import defaultdict

def calculateMeanAndMode(inputNums: List[int]) -> List[int]:
    
    mean = floor(sum(inputNums) / len(inputNums))

    d = defaultdict(int)

    for n in inputNums:
        d[n] += 1

    max_freq = max(d.values())

    return [mean, max_freq]

assert(calculateMeanAndMode([1, 2, 7, 3, 2]) == [3, 2])
    