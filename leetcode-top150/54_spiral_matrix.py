class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return None

        output = []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            # Top row
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1

            # Right col
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Bottom row
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Left col
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1

        return output

            
# Medium. Besure to add the conditions for bottom row and left col to avoid duplicate processing.
# Time: O(rows*cols)
# Space: O(rows*cols) for output list