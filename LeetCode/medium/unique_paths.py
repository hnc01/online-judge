'''
    https://leetcode.com/problems/unique-paths/

    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    How many possible unique paths are there?
'''

'''
    Time Limit Exceeded: we need to memorize the number of paths out of a certain cell if we've already seen it
'''


class Solution:
    def unique_path_helper(self, m, n, row, col):
        if row == m - 1 and col == n - 1:
            return 1
        else:
            right_path = down_path = 0
            # we need to check if we can still reach the finish cell
            if col < n - 1:
                # we can still go right
                right_path = self.unique_path_helper(m, n, row, col + 1)

            if row < m - 1:
                down_path = self.unique_path_helper(m, n, row + 1, col)

            return right_path + down_path

    def uniquePaths(self, m: int, n: int) -> int:
        return self.unique_path_helper(m, n, 0, 0)


'''
    Accepted
'''


class Solution2:
    def unique_path_helper(self, m, n, row, col, memo):
        if row == m - 1 and col == n - 1:
            return 1
        elif str(row) + "," + str(col) in memo:
            return memo[str(row) + "," + str(col)]
        else:
            right_path = down_path = 0
            # we need to check if we can still reach the finish cell
            if col < n - 1:
                # we can still go right
                right_path = self.unique_path_helper(m, n, row, col + 1, memo)

            if row < m - 1:
                down_path = self.unique_path_helper(m, n, row + 1, col, memo)

            memo[str(row) + "," + str(col)] = right_path + down_path

            return right_path + down_path

    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        return self.unique_path_helper(m, n, 0, 0, memo)


print(Solution2().uniquePaths(23, 12))
