'''
    https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

    2128. Remove All Ones With Row and Column Flips

    You are given an m x n binary matrix grid.

    In one operation, you can choose any row or column and flip each value in that row or column
    (i.e., changing all 0's to 1's, and all 1's to 0's).

    Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.
'''

'''
    look for opposite rows and then look for opposite columns then perform a flip across all 1 columns and all 1 rows.

    opposite rows or column would be equal when one is flipped (i.e. 0s -> 1s and 1s -> 0s)

    on the way, flip 'all 1' rows or cols to become all 0s
'''

'''
    Accepted. It's all a matter of skipping as much cases as possible.
'''


class Solution:
    def removeOnes(self, grid: [[int]]) -> bool:
        m = len(grid)  # number of rows
        n = len(grid[0])  # number of cols => we are guaranteed to have at least one col

        all_ones_row = '1' * n  # all 1s row means 1 across all cols => * n
        all_ones_col = '1' * m  # all 1s col means 1 across all rows => * m
        all_zeros_col = '0' * m
        all_zeros_row = '0' * n

        # look for opposite rows and flip them
        for i in range(0, m):
            current_row = ''.join('1' if bit == 1 else '0' for bit in grid[i])

            # if the current row is all 1s the we should leave it alone because we don't want
            # to risk flipping an all 0s row into 1s
            # if the current row is all 0s then we should also leave it alone because it would only
            # match with all 1s row and we don't need to change anything about that row
            if current_row != all_ones_row and current_row != all_zeros_row:
                for j in range(i + 1, m):
                    # flipping the row to see if its opposite is equal to current row
                    other_row = ''.join('1' if bit == 0 else '0' for bit in grid[j])

                    if current_row == other_row:
                        # flip the other row to become equal to current row
                        for k in range(0, n):
                            if grid[j][k] == 0:
                                grid[j][k] = 1
                            else:
                                grid[j][k] = 0

                        # no need to process any rows after other_row because other_row is now equal to current_row
                        # so when it's time to process other_row on its own, we will end up comparing it with the rows
                        # we're skipping now
                        break

        # look for opposite cols and flip them
        for i in range(0, n):
            current_col = [str(grid[x][i]) for x in range(0, m)]
            current_col = ''.join(current_col)

            # if the current col is all 1s the we should leave it alone because we don't want
            # to risk flipping an all 0s col into 1s
            # if the current col is all 0s then we should also leave it alone because it would only
            # match with all 1s col and we don't need to change anything about that col

            if current_col != all_ones_col and current_col != all_zeros_col:
                # now we go over all subsequent cols to look for opposite ones
                for j in range(i + 1, n):
                    # flipping the col to see if its opposite is equal to current col
                    other_col = [grid[x][j] for x in range(0, m)]
                    other_col = ''.join(['1' if bit == 0 else '0' for bit in other_col])

                    if current_col == other_col:
                        # flip the other col to become equal to current col
                        for k in range(0, m):
                            if grid[k][j] == 0:
                                grid[k][j] = 1
                            else:
                                grid[k][j] = 0

                        # no need to process any col after other_col because other_col is now equal to current_col
                        # so when it's time to process other_col on its own, we will end up comparing it with the cols
                        # we're skipping now
                        break

        # now that we're done, we flip all rows that are all 1s
        for i in range(0, m):
            current_row = ''.join('1' if bit == 1 else '0' for bit in grid[i])

            if current_row == all_ones_row:
                # flip the current row to 0s
                for k in range(0, n):
                    grid[i][k] = 0

        # then we flip all cols that are all 1s
        # from this step we can know whether we'll end up with leftover 1s or not
        for i in range(0, n):
            current_col = [str(grid[x][i]) for x in range(0, m)]
            current_col = ''.join(current_col)

            # when we are at last case, we don't need to do the actual flipping
            # in this case, every all 0s or all 1s column is accepted because all 0s
            # is already accepted and all 1s can be flipped.
            # the only problematic columns would be the ones that are not all 0s and not all 1s.
            if (current_col != all_ones_col) and (current_col != all_zeros_col):
                return False

        # we were not able to find any 1s so return True
        return True


# print(Solution().removeOnes(grid=[[0, 1, 0], [1, 0, 1], [0, 1, 0]]))
# print(Solution().removeOnes(grid=[[1, 1, 0], [0, 0, 0], [0, 0, 0]]))
# print(Solution().removeOnes(grid=[[0]]))
# print(Solution().removeOnes(grid=[[1,0,1],[1,0,1],[1,0,1]]))
print(Solution().removeOnes(grid=[[1, 1, 0, 0, 0]]))
