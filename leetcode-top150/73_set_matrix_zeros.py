class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # save the postions that need to be set to zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # set rows to zero
        for r in zero_rows:
            matrix[r] = [0] * cols

        # set cols to zero
        for c in zero_cols:
            for i in range(rows):
                matrix[i][c] = 0


# Medium.
# Time: O(rows*cols)
# Space: O(rows + cols)

# Follow up: O(1) space
# Use flag to record if first row and first col has zero.
# Use first row and first col as markers