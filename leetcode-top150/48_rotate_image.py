class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        top = 0
        bottom = n - 1

        # vertical reversal
        while top < bottom:
            for col in range(n):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        # Transpose
        for row in range(n):
            for col in range(row+1, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        return matrix
    
# Medium. 
# Time: reverse vertically takes O(N/2 * N) = O(N sq), transpose takes O(N/2 * N) = O(N sq). Total: O(N sq)
# Space: O(1)