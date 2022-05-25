'''
    https://leetcode.com/problems/maximum-number-of-points-with-cost/

    1937. Maximum Number of Points with Cost

    You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

    To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

    However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

    Return the maximum number of points you can achieve.

    abs(x) is defined as:

    x for x >= 0.
    -x for x < 0.
'''


class Solution:
    def maxPoints(self, points: [[int]]) -> int:
        m = len(points)  # number of rows
        n = len(points[0])  # number of cols => from given we know we have at least 1 row

        # at the beginning the previous max score is the first row
        previous_max_scores = points[0]

        for row in range(1, m):
            current_max_scores = [0] * n

            for col in range(0, n):
                # we need to check the different ways we can get to cell [row][col] from each point in previous_max_scores
                for i in range(0, n):
                    parent = previous_max_scores[i]

                    # to reach the current cell from parent, the score is: parent + cell[row][col] - abs(col - i)
                    score = parent + points[row][col] - int(abs(col - i))

                    current_max_scores[col] = max(current_max_scores[col], score)

            previous_max_scores = current_max_scores

        # at the end it's the max in the last row
        return max(previous_max_scores)


'''
    The optimized DP solution will allow us to compute the scores of each row in one go instead of calculating the score of each individually.
    
    The idea is that when we have a row [0 .. j] [j+1 .. n]: to calculate the score of a cell at [j], we can use the score of cell [j-1]. Because
    the score of [j] and [j-1] is the same except that [j] would have -1 of the score since it's further 1 cell from [j-1]. 
'''


class Solution2:
    def maxPoints(self, points: [[int]]) -> int:
        m = len(points)  # number of rows
        n = len(points[0])  # number of cols => from given we know we have at least 1 row

        # just like in Solution, we only need the previous row in our calculations
        # and, at the beginning, the row of previous results is equal to first row in points
        previous_row_max_scores = points[0]

        # when going from a cell in row i-1 to a cell in row i, we can come in 3 directions:
        # - Down (no need for extensive calculations - can be factored in quickly)
        # - from the Left
        # - from the right
        left = [0] * n
        right = [0] * n

        # for the first row (at 0) in points, the max score at each cell points[i][j]
        # is equal to points[i][j] so we don't include it in our logic
        for i in range(1, m):
            # when going from left to right, it means that the cell in i-1 is to the left of current cell in row i
            # this means that we need fill the left array
            # left[j] = max(left[j-1] - 1, previous_row_max_scores[j])
            for j in range(0, n):
                if j == 0:
                    # there are no cells above the current one to the left, so the only solution to reach this cell is to
                    # come down from cell directly above
                    left[j] = previous_row_max_scores[j]
                else:
                    # previous_row_max_scores[j] => coming down from cell above
                    # left[j-1] - 1 => coming down from cell to the left
                    left[j] = max(left[j - 1] - 1, previous_row_max_scores[j])

            # when going from right to left, it means that the cell in i-1 is to the right of current cell in row i
            # this means that we need fill the right array
            # right[j] = max(right[j+1] - 1, previous_row_max_scores[j])
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    # there's nothing above it to its right, so the only solution to reach this cell is to
                    # come down from cell directly above
                    right[j] = previous_row_max_scores[j]
                else:
                    right[j] = max(right[j + 1] - 1, previous_row_max_scores[j])

            # now that we are done with computing max score in all directions, we need to save the max scores only for each cell
            for j in range(0, n):
                previous_row_max_scores[j] = max(right[j], left[j]) + points[i][j]

        return max(previous_row_max_scores)


print(Solution2().maxPoints(points=[[1, 2, 3], [1, 5, 1], [3, 1, 1]]))
print(Solution2().maxPoints(points=[[1, 5], [2, 3], [4, 2]]))
print(Solution2().maxPoints(points=[[0]]))
print(Solution2().maxPoints(points=[[3]]))
print(Solution2().maxPoints(points=[[0, 3, 0, 4, 2], [5, 4, 2, 4, 1], [5, 0, 0, 5, 1], [2, 0, 1, 0, 3]]))
print(Solution2().maxPoints(points=[
    [8, 2, 4, 4, 9, 3, 5, 3, 10, 10],
    [4, 8, 7, 4, 0, 1, 10, 6, 4, 0],
    [0, 5, 2, 10, 4, 2, 7, 8, 6, 8],
    [0, 1, 1, 2, 8, 0, 5, 9, 8, 2],
    [6, 2, 0, 4, 5, 0, 5, 3, 10, 3]]))
