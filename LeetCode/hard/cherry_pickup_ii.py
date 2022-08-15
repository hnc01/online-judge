'''
    https://leetcode.com/problems/cherry-pickup-ii/

    1463. Cherry Pickup II

    You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number
    of cherries that you can collect from the (i, j) cell.

    You have two robots that can collect cherries for you:
        - Robot #1 is located at the top-left corner (0, 0), and
        - Robot #2 is located at the top-right corner (0, cols - 1).

    Return the maximum number of cherries collection using both robots by following the rules below:
        - From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
        - When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
        - When both robots stay in the same cell, only one takes the cherries.
        - Both robots cannot move outside of the grid at any moment.
        - Both robots should reach the bottom row in grid.
'''

'''
    Accepted
'''

class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        # 2 <= rows, cols <= 70
        rows = len(grid)
        cols = len(grid[0])

        def helper(r1Row, r1Col, r2Row, r2Col, grid, memo):
            # if we exceed the bounds of our grid we return 0 cherries
            if r1Row < 0 or r2Row < 0 or r1Col < 0 or r2Col < 0 or r1Row >= rows or r2Row >= rows or r1Col >= cols or r2Col >= cols:
                return 0
            elif (r1Row, r1Col, r2Row, r2Col) in memo:
                return memo[(r1Row, r1Col, r2Row, r2Col)]
            else:
                # get the current cell's score
                if (r1Row, r1Col) == (r2Row, r2Col):
                    score = grid[r1Row][r1Col]
                else:
                    score = grid[r1Row][r1Col] + grid[r2Row][r2Col]

                oldValue = {
                    (r1Row, r1Col): grid[r1Row][r1Col],
                    (r2Row, r2Col): grid[r2Row][r2Col]
                }

                # we need to lay out our possible moves
                r1Moves = [(r1Row + 1, r1Col - 1), (r1Row + 1, r1Col), (r1Row + 1, r1Col + 1)]
                r2Moves = [(r2Row + 1, r2Col - 1), (r2Row + 1, r2Col), (r2Row + 1, r2Col + 1)]

                maxScore = 0

                for i in range(0, len(r1Moves)):
                    for j in range(0, len(r2Moves)):
                        r1NextRow, r1NextCol = r1Moves[i]
                        r2NextRow, r2NextCol = r2Moves[j]

                        maxScore = max(maxScore, helper(r1NextRow, r1NextCol, r2NextRow, r2NextCol, grid, memo))

                # backtracking by putting back the value like we found in grid so we can explore other options
                grid[r1Row][r1Col] = oldValue[(r1Row, r1Col)]
                grid[r2Row][r2Col] = oldValue[(r2Row, r2Col)]

                memo[(r1Row, r1Col, r2Row, r2Col)] = score + maxScore

                return score + maxScore

        memo = {}

        return helper(0, 0, 0, cols - 1, grid, memo)

grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]

print(Solution().cherryPickup(grid))