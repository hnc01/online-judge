'''
    https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

    562. Longest Line of Consecutive One in Matrix

    Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

    The line could be horizontal, vertical, diagonal, or anti-diagonal.
'''

'''
    Accepted
'''


class Solution:
    def longestLine(self, mat: [[int]]) -> int:
        # maps each point (i,j) to the length of longest consecutive 1s in each direction
        # goes right
        horizontal = {}
        # goes down
        vertical = {}
        # goes right down
        diagonal = {}
        # goes left down
        anti_diagonal = {}

        # we know that 1 <= m,n so below is safe to do
        m = len(mat)
        n = len(mat[0])

        # length of longest sequence of consecutive ones
        max_length = 0

        def getLongestLineAtPoint(i, j):
            nonlocal max_length, mat, horizontal, vertical, diagonal, m, n

            # we check horizontally to the right
            # by default, since current (i,j) == 1 then horizontal[(i,j)] = 1
            horizontal[(i, j)] = 1

            if j + 1 < n and mat[i][j + 1] == 1:
                # check the longest `horizontal` for (i, j+1)
                # and do +1 for it to get the longest horizontal for (i,j)
                horizontal[(i, j)] = horizontal[(i, j + 1)] + 1

            max_length = max(max_length, horizontal[(i, j)])

            # we check vertically down
            # by default, since current (i,j) == 1 then vertical[(i,j)] = 1
            vertical[(i, j)] = 1

            if i + 1 < m and mat[i + 1][j] == 1:
                # check the longest `vertical` for (i + 1, j)
                # and do +1 for it to get the longest vertical for (i,j)
                vertical[(i, j)] = vertical[(i + 1, j)] + 1

            max_length = max(max_length, vertical[(i, j)])

            # we check diagonally right down
            # by default, since current (i,j) == 1 then diagonal[(i,j)] = 1
            diagonal[(i, j)] = 1

            if (i + 1 < m and j + 1 < n) and mat[i + 1][j + 1] == 1:
                diagonal[(i, j)] = diagonal[(i + 1, j + 1)] + 1

            max_length = max(max_length, diagonal[(i, j)])

            # we check diagonally left down
            anti_diagonal[(i, j)] = 1

            if (i + 1 < m and j - 1 >= 0) and mat[i + 1][j - 1] == 1:
                anti_diagonal[(i, j)] = anti_diagonal[(i + 1, j - 1)] + 1

            max_length = max(max_length, anti_diagonal[(i, j)])

        # since we check to the right of each point and under each point
        # it's better if we start building our memos from the bottom right
        # corner of the matrix. That way, we'd have our results ready for us
        # as we go through the matrix
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # we don't care about points that are 0
                if mat[i][j] == 1:
                    getLongestLineAtPoint(i, j)

        return max_length


# print(Solution().longestLine(mat=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]))
# print(Solution().longestLine(mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]))
# print(Solution().longestLine(mat = [[1]]))
# print(Solution().longestLine(mat = [[0]]))
print(Solution().longestLine(
    [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]))
