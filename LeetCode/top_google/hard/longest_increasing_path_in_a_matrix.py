'''
    https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

    329. Longest Increasing Path in a Matrix

    Given an m x n integers matrix, return the length of the longest increasing path in matrix.

    From each cell, you can either move in four directions: left, right, up, or down. You may not move
    diagonally or move outside the boundary (i.e., wrap-around is not allowed).
'''


class Solution:
    def longestIncreasingPathHelper(self, matrix, i, j, m, n, isVisited, longestPathLengthFromCell):
        # first we check if the current cell we need to proceed with already has computed results
        if (i, j) in longestPathLengthFromCell:
            return longestPathLengthFromCell[(i, j)]

        isVisited[i][j] = True

        # if we don't have results for it then we need to compute it by visiting its neighboring cells
        # and seeing which ones we can proceed with
        neighbors = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]

        # we start with maxPathLength = 1 to mark the length is at least as long as this cell => 1
        maxPathLength = 1

        for x, y in neighbors:
            # check if cell is within the boundaries AND if it's increasing path AND not visited yet
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j] and not isVisited[x][y]:
                # it's a path we can explore
                currentPathLength = 1 + self.longestIncreasingPathHelper(matrix, x, y, m, n, isVisited, longestPathLengthFromCell)

                maxPathLength = max(maxPathLength, currentPathLength)

                # now we backtrack by marking this cell as not visited so we can visit another path
                isVisited[x][y] = False

        longestPathLengthFromCell[(i, j)] = maxPathLength

        return maxPathLength

    def longestIncreasingPath(self, matrix: [[int]]) -> int:
        m = len(matrix)  # rows
        n = len(matrix[0])  # cols

        # to keep track of longest path
        longestPathLength = float('-inf')

        # this will map every cell to the longest path we can make from it
        # this will prevent us from recomputing the same lengths over and over
        longestPathLengthFromCell = {}

        # then we need to go over every cell and see what's the longest
        # increasing path we can get from it
        for i in range(0, m):
            for j in range(0, n):
                # initially, all cells are not visited
                isVisited = [[]] * m

                for k in range(0, m):
                    isVisited[k] = [False] * n

                cellMaxLength = self.longestIncreasingPathHelper(matrix, i, j, m, n, isVisited, longestPathLengthFromCell)

                longestPathLength = max(longestPathLength, cellMaxLength)

        return longestPathLength

print(Solution().longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]]))
print(Solution().longestIncreasingPath(matrix = [[3,4,5],[3,2,6],[2,2,1]]))
print(Solution().longestIncreasingPath(matrix = [[1]]))