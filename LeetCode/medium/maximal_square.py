'''
    https://leetcode.com/problems/maximal-square/

    221. Maximal Square

    Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''

'''
    Accepted: DP with memoization (top-down)
'''


class Solution:
    def maximal_square_helper(self, matrix, m, n, i, j, memo):
        if i >= m or j >= n:
            # when we exceed the bounds we can't produce any square
            return 0

        if (i, j) in memo:
            return memo[(i, j)]
        else:
            if matrix[i][j] == '1':
                current_max_length = 1 + int(min(
                    self.maximal_square_helper(matrix, m, n, i + 1, j + 1, memo),
                    self.maximal_square_helper(matrix, m, n, i + 1, j, memo),
                    self.maximal_square_helper(matrix, m, n, i, j + 1, memo)))

                memo[(i, j)] = current_max_length

                return current_max_length
            else:
                return 0

    def maximalSquare(self, matrix: [[str]]) -> int:
        memo = {}

        m = len(matrix)  # rows
        n = len(matrix[0])  # cols

        largest_so_far = 0

        for i in range(0, m):
            for j in range(0, n):
                # we can make a square at (i,j) if: (i,j) is '1' and there are squares across all its neighbours (i+1, j+1), (i+1,j), (i,j+1)
                # but we can expand the square at (i,j) by one according to the smallest square that can be formed by its neighbours
                current_max_length = self.maximal_square_helper(matrix, m, n, i, j, memo)

                largest_so_far = int(max(current_max_length, largest_so_far))

        return largest_so_far * largest_so_far


'''
    Accepted: DP bottom-up
'''


class Solution2:
    def maximalSquare(self, matrix: [[str]]) -> int:
        m = len(matrix)  # rows
        n = len(matrix[0])  # cols

        # initializing the dp array
        dp = [[]] * (m + 1)

        for row in range(0, m + 1):
            dp[row] = [0] * (n + 1)

        # the base case is when we exceed the length so we need account for that in our dp structure => dp[m][...] = 0 and dp[...][n] = 0
        for col in range(0, n + 1):
            dp[m][col] = 0

        for row in range(0, m + 1):
            dp[row][n] = 0

        largest_so_far = 0

        # in the memoization approach we index (i+1, j+1), (i+1,j) and (i,j+1) which means that we need these solved before (i,j)
        # this means we need to loop the matrix from bottom right corner and go back until the top left corner
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + int(min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1]))

                    largest_so_far = int(max(largest_so_far, dp[i][j]))
                # else it remains 0 as per the initialization step

        return largest_so_far * largest_so_far


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1"]]

matrix = [["0", "1"], ["1", "0"]]

matrix = [["0"]]

print(Solution2().maximalSquare(matrix))
