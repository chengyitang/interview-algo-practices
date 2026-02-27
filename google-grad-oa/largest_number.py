"""
There is an array, named digits, consisting of N digits.
Choose at most three digits (not necessarily adjacent) and merge them into a new integer without changing the order of the digits.
What is the biggest number that can be obtained this way?

Write a function that, given an array of N digits, return the biggest number that can be built.

Examples:
1. Given digits = [7,2,3,3,4,9], the function should return 749.
2. Given digits = [0,0,5,7], the function should return 57.

Constraints:
1. N is an integer within the range [3..50]
2. each element of array, named digits, is an integer within the range [0..9]

"""

def solution(digits):

    """
    Given those constraints, we can use a greedy approach with O(N^3) time complexity, which is acceptable.
    """

    max_number = 0

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            for k in range(j + 1, len(digits)):
                current_number = digits[i] * 100 + digits[j] * 10 + digits[k]
                max_number = max(max_number, current_number)

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            current_number = digits[i] * 10 + digits[j]
            max_number = max(max_number, current_number)

    for i in range(len(digits)):
        current_number = digits[i]
        max_number = max(max_number, current_number)

    return max_number

# Time: O(N^3) worst case: 48^3 = 110592
# Space: O(1) max_number