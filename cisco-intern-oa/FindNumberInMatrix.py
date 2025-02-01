def funcMatrix(matrix):
    if not matrix:
        return -1
    
    rows, cols = len(matrix), len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            # check if largest in row
            is_largest = True
            for col in range(cols):
                if matrix[r][c] < matrix[r][col]: # not largest in row
                    is_largest = False
                    break
            # check if smallest in col
            is_smallest = True
            for row in range(rows):
                if matrix[r][c] > matrix[row][c]: # not smallest in col
                    is_smallest = False
                    break

            # if both valid: found
            if is_largest and is_smallest:
                return matrix[r][c]
            
    return -1
            
                