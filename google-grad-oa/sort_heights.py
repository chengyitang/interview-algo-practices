"""
Problem Description:

Given an array A representing student heights. All students must form into several lines, arriving in the order they appear in the array.

For the i-th student:

If there exists a line where all students in that line are taller than A[i], the student may join any such line.
If no such line exists, the student must start a new line.
Compute the minimum number of lines that will be created.

Write a function that, given a non-empty integer array A (length N), returns the minimum number of lines.
"""

def solution(A):

    if not A:
        return 0

    tails = []

    for height in A:
        if not tails:
            tails.append(height)
        else:
            # do binary search to find the correct line
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] <= height:
                    l = mid + 1
                else:
                    r = mid - 1
            if l == len(tails): # no line meeting the condition, start a new line
                tails.append(height)
            else: # join the line
                tails[l] = height
    return len(tails)

# Greedy + Binary Search
# Time: O (N log N)
# Space: O (N)

print(solution([1, 2, 3, 4, 5])) # 5
print(solution([5, 4, 3, 2, 1])) # 1
print(solution([1, 3, 2, 4, 5])) # 4
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 10
print(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # 1
print(solution([5, 2, 4, 3, 1, 6])) # 3
print(solution([5, 5, 5])) # 3