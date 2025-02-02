def maximumPossibleEvenSum(val):
    n = len(val)
    max_even_sum = 0
    
    # Function to find maximum even sum using subset combinations
    def find_combinations(index, current_sum):
        nonlocal max_even_sum
        
        # Base case: reached end of array
        if index == n:
            # If current sum is even, update max_even_sum if needed
            if current_sum % 2 == 0:
                max_even_sum = max(max_even_sum, current_sum)
            return
        
        # Don't include current element
        find_combinations(index + 1, current_sum)
        
        # Include current element
        find_combinations(index + 1, current_sum + val[index])
    
    find_combinations(0, 0)
    return max_even_sum


assert(maximumPossibleEvenSum([2, 3, 6, -5, 10, 1, 1]) == 22)

# Backtracking problem