'''
    https://leetcode.com/problems/minimum-path-sum/

    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.
'''

'''
    Time limit exceeded
'''


class Solution:
    def min_path_sum_helper(self, grid, m, n, row, col):
        if row == m - 1 and col == n - 1:
            # we reached the last cell
            return grid[row][col]
        else:
            down_path = right_path = float("inf")

            if row < m - 1:
                # we can keep going down
                down_path = self.min_path_sum_helper(grid, m, n, row + 1, col)

            if col < n - 1:
                right_path = self.min_path_sum_helper(grid, m, n, row, col + 1)

            return grid[row][col] + int(min(down_path, right_path))

    def minPathSum(self, grid: [[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        return self.min_path_sum_helper(grid, m, n, 0, 0)


'''
    Accepted
'''


class Solution2:
    def min_path_sum_helper(self, grid, m, n, row, col, memo):
        if row == m - 1 and col == n - 1:
            # we reached the last cell
            return grid[row][col]
        elif str(row) + "," + str(col) in memo:
            return memo[str(row) + "," + str(col)]
        else:
            down_path = right_path = float("inf")

            if row < m - 1:
                # we can keep going down
                down_path = self.min_path_sum_helper(grid, m, n, row + 1, col, memo)

            if col < n - 1:
                # we can keep going right
                right_path = self.min_path_sum_helper(grid, m, n, row, col + 1, memo)

            min_sum = grid[row][col] + int(min(down_path, right_path))

            memo[str(row) + "," + str(col)] = min_sum

            return min_sum

    def minPathSum(self, grid: [[int]]) -> int:
        memo = {}

        m = len(grid)
        n = len(grid[0])

        return self.min_path_sum_helper(grid, m, n, 0, 0, memo)


print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]))
