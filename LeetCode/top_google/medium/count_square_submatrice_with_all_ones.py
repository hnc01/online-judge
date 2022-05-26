'''
    https://leetcode.com/problems/count-square-submatrices-with-all-ones/

    1277. Count Square Submatrices with All Ones


    Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
'''

'''
    Accepted.
'''


class Solution:
    def countSquares(self, matrix: [[int]]) -> int:
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of cols

        # we will use a dp solution. Each dp[i][j] represents the max number of squares
        # we can make with matrix[i][j] as top left corner
        # dp has to be same dimensions as matrix
        dp = [[]] * (m + 1)  # to make the computations easier, we need to be able to index m in dp just to
        # account for edge cases where j+1 or i+1 are outside the borders of our matrix. These edge cases will remain
        # with default value 0

        # by default, each cell can make 0 squares before we start computations
        for i in range(0, m + 1):
            dp[i] = [0] * (n + 1)  # to make the computations easier, we need to be able to index m in dp just to
        # account for edge cases where j+1 or i+1 are outside the borders of our matrix. These edge cases will remain
        # with default value 0

        totalMatrices = 0

        # we need to traverse the matrix from bottom right corner to the top
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # for each cell, we will check the cell at [i][j+1], [i+1][j+1] and [i+1][j]
                # because each of these might contribute to the squares that can be created with
                # [i][j] as top left corner
                # we will choose the min([i][j+1], [i+1][j+1], [i+1][j]) so that we don't end up with rectangles

                # we only process the cells that have matrix[i][j] == 1
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j + 1], dp[i + 1][j + 1], dp[i + 1][j]) + 1  # we add the plus to account for the single
                    # matrix that can be formed by the cell [i][j] alone

                    # we won't be altering this value again so we can proceed with adding it to our total
                    totalMatrices += dp[i][j]

        return totalMatrices


print(Solution().countSquares(matrix=
[
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))

print(Solution().countSquares(matrix=
[
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))
