

''' 
given array of integers numbers. Return the difference between the sum 
of all even-positioned-elemnets with values between -100 to 100 (inclusive) 
and the sum of all odd-positioned elements
with values that lie within the same range

time complexity not worse than O(len(numbers) ^ 2)
'''

from collections import defaultdict


def solution(nums):
    even_sum = odd_sum = 0

    for i in range(len(nums)):
        if i % 2 == 0 and -100 <= nums[i] <= 100: # odd
            odd_sum += nums[i]
        elif i % 2 != 0 and -100 <= nums[i] <= 100: # even
            even_sum += nums[i]
    return odd_sum - even_sum


'''
Given a list of student grades (1~5) records in the following format: "[name]:[grade]"
, find the student with the highest avg grade. It's guaranteed that all studens have
different avg. grades.

No spaces in names.
TC not worse than O(n^3)
'''
def solution1(records):
    grades = defaultdict(lambda: [0, 0])
    for nameGrade in records:
        name, grade = nameGrade.split(": ")
        grades[name][0] += int(grade)
        grades[name][1] += 1

    maxAvg = 0
    maxAvgStu = None
    for student, gradeInfo in grades.items():
        if gradeInfo[0] / gradeInfo[1] > maxAvg:
            maxAvg = gradeInfo[0] / gradeInfo[1]
            maxAvgStu = student
    return maxAvgStu


def solution2(orchard, days):  # bfs

    rows, cols = len(orchard), len(orchard[0])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for _ in range(days):

        will_rot = set()

        for r in range(rows):
            for c in range(cols):
                if orchard[r][c] == "R":
                    for dr, dc in directions:
                        if (r + dr) in range(rows) and (c + dc) in range(cols) and orchard[r + dr][c + dc] == "T":
                            will_rot.add((r + dr, c + dc))

        for r, c in will_rot:
            orchard[r][c] = "R"
    return orchard

''' In a retail store, you're in charge of analyziing patterns in product sales to optimized inventory. You
have an array of positive integers, salesData, where each integer represents the sales amount on a given day.
Additionally, you have a positive integer frequencyThreshold, which is specifies the maximum allowed frequency of
any sales amount within a contiguous subarray

Find the longest contiguous subarray where no sales amount appears more times than the frequencyThreshold.
Return integer indicating the length of the longest such subarray.
'''

def longestSubarrayWithMaximum(salesData, frequencyThreshold):

    mp = defaultdict(int)
    l, r = 0, 0
    ret = 0

    while r < len(salesData):
        mp[salesData[r]] += 1
        
        while mp[salesData[r]] > frequencyThreshold:
            mp[salesData[l]] -= 1
            l += 1

        ret = max(ret, r - l + 1)
        r += 1

    return ret

def serverTime(startupTime, shutdownTime, currentTime):
    start, shut = [], []
    for time in startupTime:
        hr, m = time.split(':')
        start.append(int(hr) * 60 + int(m))
    for time in shutdownTime:
        if time == "None":
            shut.append("None")
            continue
        hr, m = time.split(':')
        shut.append(int(hr) * 60 + int(m))

    hr, m = currentTime.split(':')
    cur = int(hr) * 60 + int(m)
    ret = 0

    for i in range(len(start)):
        if shut[i] == "None":
            ret += cur - start[i]
        else:
            ret += shut[i] - start[i]
    
    return ret

def schedule():
    pass

''' 
Image that you have a time machine. you are given an array years. You start in the year years[0]
You start in the years[0]. First, you want travel to years[1] then years[2], and so on.
Your task is to calculate the time required to visit all the years from the list in order.

Time required:
A = B: 0 hr
A < B: 1 hr
A > B: 2 hr
'''

def timeMachine(years):
    time = 0
    for i in range(1, len(years)):
        if years[i - 1] == years[i]:
            continue
        elif years[i - 1] < years[i]:
            time += 1
        else:
            time += 2
    return time

'''
Given an array lamps where lamp[i] covers the range of light from lamp[i][0] to lamp[i][1] and an array of points, return an array having the number of illumination sources or overlaps for each of the points.
eg:
lamps = [[1, 4], [2, 6], [8, 10]]
points = [2, 4, 5, 7, 9]
ans = [2, 2, 1, 0, 1]
'''
def lampIlluminated(lamps, benches):
    # 0 -> on
    # 1 -> bench
    # 2 -> off
    ''' Sweep algo '''

    events = [] 

    for lamp in lamps:
        events.append([0 ,lamp[0]]) # on
        events.append([2, lamp[1] + 1]) # off

    for bench in benches:
        events.append([1, bench])

    events.sort(key=lambda x: x[1]) # sort by axis

    # Track events
    answer = []
    lampsOn = 0
    for type, axis in events:
        if type == 0:
            lampsOn += 1
        elif type == 2:
            lampsOn -= 1
        else:
            answer.append(lampsOn)
    return answer

    # O(n log n): n = len(events)
    # O(len(benches))

def compare(nums, pivot):
    greater = smaller = 0
    for n in nums:
        if n > pivot:
            greater += 1
        elif n < pivot:
            smaller += 1
        else:
            continue
    
    if greater > smaller:
        return "greater"
    elif greater < smaller:
        return "smaller"
    else:
        return "tie"
    
def object_collision(centers):

    def check_collision(obj1, obj2):
        x1, y1 = obj1
        x2, y2 = obj2
        return abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2

    collsions = 0

    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            if check_collision(centers[i], centers[j]):
                collsions += 1
    return collsions


if __name__ == "__main__":
    assert solution([101, 3, 4, 359, 2, 5]) == -2
    assert solution([-2, 234, 100, 99, 540, -1]) == 0
    print("Pass!")

    assert solution1(["John: 5", "Michael: 4", "Ruby: 2", "Ruby: 5", "Michael: 5"]) == "John"
    assert solution1(["Kate: 5", "Kate: 5", "Maria: 2", "John: 5", "Michael: 4", "John: 4"]) == "Kate"
    print("Pass!")

    orchard = [
        ["T", "T", "R", "-"],
        ["T", "T", "T", "T"],
        ["-", "T", "-", "R"]
    ]
    expected = [
        ["R", "R", "R", "-"],
        ["R", "R", "R", "R"],
        ["-", "R", "-", "R"]
    ]

    assert solution2(orchard, 3) == expected
    print("Pass!")

    assert longestSubarrayWithMaximum([1, 2, 1, 3, 2], 1) == 3
    assert longestSubarrayWithMaximum([1], 1) == 1
    print("Pass!")

    assert serverTime(["12:30", "14:00", "19:55"], ["15:00", "17:00", "None"], "20:00") == 335
    print("Pass!")

    assert timeMachine([2000, 1990, 2005, 2050]) == 4
    print("Pass!")

    assert lampIlluminated([[1, 4], [2, 6], [8, 10]], [2, 4, 5, 7, 9]) == [2, 2, 1, 0, 1]
    print("Pass!")

    assert compare([1, 3, 0, -1, 1, 4, 3], 2) == "smaller"
    assert compare([3, 4, 5, 1, 0], 3) == "tie"
    print("Pass!")

    assert object_collision([[1, 1], [2, 2], [0, 4]]) == 2
    print("Pass!")