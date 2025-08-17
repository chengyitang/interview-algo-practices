"""
Alternating Parity Pattern Problem

DESCRIPTION:
An array follows an alternating parity pattern if it does not contain two consecutive integers 
of the same parity. In simpler terms, there are never two consecutive even numbers nor two 
consecutive odd numbers.

TASK:
Given an array of non-negative integers named `numbers`:
- Determine if there are elements that break the alternating parity pattern
- Return the index of the FIRST element where the alternating parity pattern breaks
- If no such elements exist (i.e., the array perfectly follows the pattern), return `-1`

CONSTRAINTS:
- The input `numbers` array contains non-negative integers
- A solution with time complexity not worse than O(numbers.length^2) is expected to fit within 
  the execution time limit
- The most optimal solution is not necessarily required

EXAMPLES:

Example 1:
Input: numbers = [1, 2, 5, 3, 6]
Expected Output: solution(numbers) = 3
Explanation:
- 1 (odd)
- 2 (even) - 1 and 2 alternate
- 5 (odd) - 2 and 5 alternate  
- 3 (odd) - 5 and 3 are both odd. This breaks the pattern
- Since both numbers[2] = 5 and numbers[3] = 3 are odd, the first index where the alternating 
  parity pattern breaks is numbers[3]

Example 2:
Input: numbers = [1, 4, 7, 2, 5, 6]
Expected Output: solution(numbers) = -1
Explanation:
- 1 (odd)
- 4 (even)
- 7 (odd)
- 2 (even)
- 5 (odd)
- 6 (even)
- All elements follow the alternating parity pattern, so there are no indices where the pattern breaks

ALGORITHM APPROACH:
1. Iterate through the array starting from index 1
2. For each element, check if it has the same parity as the previous element
3. If same parity is found, return the current index
4. If no violation is found, return -1
"""

# Results: 
# Time complexity: O(n) - linear scan
# Space complexity: O(1) - constant space

def solution(numbers: list[int]) -> int:
    
    # Null check and edge case
    if not numbers or len(numbers) < 2:
        return -1
    
    # Sliding window approach
    for i in range(1, len(numbers)):
        if numbers[i] % 2 == numbers[i - 1] % 2: # same parity
            return i
    return -1
    
def run_tests():
    
    test_cases = [
        ([1, 2, 5, 3, 6], 3),
        ([1, 4, 7, 2, 5, 6], -1),
        ([], -1),
        ([1], -1),
        ([1, 2], -1),
        ([2, 4], 1)
    ]

    for i, (input, expected) in enumerate(test_cases):
        result = solution(input)
        if result == expected:
            print(f"Test {i} passed")
        else:
            print(f"Test {i} failed: expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()