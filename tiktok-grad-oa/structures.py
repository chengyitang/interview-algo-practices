"""
Problem Description: Harmonious Pattern Transformation

You are managing a row of building structures with varying heights, represented by an array named `structures`.

Goal: Transform these structures into a "harmonious pattern."

Harmonious Pattern Definition: Each structure must differ from its adjacent neighbors by exactly one unit in height, forming either an ascending or a descending sequence.

Allowed Operation: You can only add one unit of height to any structure in a single operation.

Objective: Determine the minimum number of operations needed to achieve either an ascending or a descending stepwise pattern. The solution should choose whichever pattern requires fewer operations.

Example 1:
Input: structures = [1, 4, 3, 2]
Expected Output: solution(structures) = 4
Optimal Approach: Add four units to the first structure.
Resulting Pattern: The final heights will be [5, 4, 3, 2], which forms a descending stepwise pattern (5-1=4, 4-1=3, 3-1=2).

Example 2:
Input: structures = [5, 7, 9, 4, 11]
Expected Output: solution(structures) = 9
Optimal Approach: 
- Add two units to the first structure.
- Add one unit to the second structure.
- Add six units to the fourth structure.
"""

def solution(structures):
    """
    Calculate the minimum operations needed to create a harmonious pattern.
    
    Args:
        structures: List[int] - Array of building heights
        
    Returns:
        int - Minimum number of operations needed
    """
    if not structures:
        return 0
    
    n = len(structures)
    if n == 1:
        return 0
    
    def get_operations_for_pattern(start_height, ascending=True):
        """Calculate operations needed for a specific pattern starting from start_height"""
        operations = 0
        
        for i in range(n):
            # Calculate target height for this position
            if ascending:
                target_height = start_height + i
            else:
                target_height = start_height - i
            
            # If current structure is shorter than target, we need to add height
            if structures[i] < target_height:
                operations += target_height - structures[i]
        
        return operations
    
    # For ascending pattern: find optimal starting height
    # The starting height should be at least max(structures[i] - i) for all i
    min_ascending_start = 0
    for i in range(n):
        min_ascending_start = max(min_ascending_start, structures[i] - i)
    
    # For descending pattern: find optimal starting height
    # The starting height should be at least max(structures[i] + i) for all i
    min_descending_start = 0
    for i in range(n):
        min_descending_start = max(min_descending_start, structures[i] + i)
    
    # Calculate operations for both patterns
    ascending_ops = get_operations_for_pattern(min_ascending_start, ascending=True)
    descending_ops = get_operations_for_pattern(min_descending_start, ascending=False)
    
    return min(ascending_ops, descending_ops)


# Test cases
if __name__ == "__main__":
    # Example 1
    test1 = [1, 4, 3, 2]
    print(f"Example 1: {test1}")
    print(f"Result: {solution(test1)}")  # Expected: 4
    print()
    
    # Example 2
    test2 = [5, 7, 9, 4, 11]
    print(f"Example 2: {test2}")
    print(f"Result: {solution(test2)}")  # Expected: 9
    print()
    
    # Additional test cases
    test3 = [1, 2, 3, 4]
    print(f"Test 3: {test3}")
    print(f"Result: {solution(test3)}")  # Expected: 0 (already ascending)
    print()
    
    test4 = [4, 3, 2, 1]
    print(f"Test 4: {test4}")
    print(f"Result: {solution(test4)}")  # Expected: 0 (already descending)
    print()
    
    test5 = [1, 1, 1, 1]
    print(f"Test 5: {test5}")
    print(f"Result: {solution(test5)}")  # Expected: 3 (make ascending: 1,2,3,4)
