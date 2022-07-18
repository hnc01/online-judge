'''
    1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

    https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

    Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four
    neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.

    Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

    A binary matrix is a matrix with all cells equal to 0 or 1 only.

    A zero matrix is a matrix with all cells equal to 0.
'''
import math


class Solution:
    def isZeroMatrix(self, mat: [[int]]):
        for i in range(0, len(mat)):
            if sum(mat[i]) != 0:
                return False

        return True

    def minFlipsHelper(self, mat, i, j, m, n):
        if self.isZeroMatrix(mat):
            # no more steps required
            return 0
        elif i >= m or j >= n:
            # we have exceeded our bottom right corner
            # => we went through all of our cells and we found
            # that we can't get a zero matrix
            return float('inf')
        else:
            # we are now at cell (i, j) we need to see if we can
            # obtain a 0 matrix by either flipping this cell or not
            flippedMat = [[]] * m

            for row in range(0, m):
                flippedMat[row] = mat[row].copy()

            # the four neighbors for cell are (i-1, j), (i+1, j), (i, j-1), (i, j+1)
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

            for cell in neighbors:
                if 0 <= cell[0] < m and 0 <= cell[1] < n:
                    flippedMat[cell[0]][cell[1]] = int(not mat[cell[0]][cell[1]])

            # flip the cell itself
            flippedMat[i][j] = int(not flippedMat[i][j])

            # moving on to the next cell => either we stay in same row and go to the right OR we start a new row
            nextCell = (i, j + 1)

            if j + 1 >= n:
                nextCell = (i + 1, 0)

            flippedResult = 1 + self.minFlipsHelper(flippedMat, nextCell[0], nextCell[1], m, n)
            notFlippedResult = self.minFlipsHelper(mat, nextCell[0], nextCell[1], m, n)

            # we examine the path of not flipping the current cell AND flipping the current cell
            return min(flippedResult, notFlippedResult)

    def minFlips(self, mat: [[int]]) -> int:
        m = len(mat)  # rows
        n = len(mat[0])  # cols

        result = self.minFlipsHelper(mat, 0, 0, m, n)

        if math.isinf(result):
            return -1

        return result


print(Solution().minFlips(mat=[[0, 0], [0, 1]]))
print(Solution().minFlips(mat=[[0]]))
print(Solution().minFlips(mat=[[1, 0, 0], [1, 0, 0]]))
print(Solution().minFlips(mat=[[0, 0, 0], [1, 1, 1]]))
print(Solution().minFlips(mat=[[1, 1, 0], [0, 0, 1]]))
