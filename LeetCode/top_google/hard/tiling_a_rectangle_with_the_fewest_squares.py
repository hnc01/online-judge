'''
    https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

    1240. Tiling a Rectangle with the Fewest Squares

    Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.
'''

'''
    Accepted
'''


class Solution:
    def findNextCell(self, grid, n, m):
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == False:
                    return (i, j)

        return (None, None)

    def findMaxSquare(self, grid, n, m, i, j):
        # since we fill squares from left to right, top to bottom
        # it's enough to find the first True to the right and first True from the bottom
        # to get the max size square that can fit with this cell as top left corner

        maxWidth = 0

        for col in range(j, m):
            if grid[i][col] == True:
                # we found our right boundary
                break
            else:
                maxWidth += 1

        maxHeight = 0

        for row in range(i, n):
            if grid[row][j] == True:
                # we found our bottom boundary
                break
            else:
                maxHeight += 1

        # the max size square that we can fit at (i, j) is the min between max height and max width
        return min(maxWidth, maxHeight)

    def fillSquare(self, grid, i, j, size, value):
        # value can be either True (when we're exploring an option) or False when we're backtracking
        for row in range(i, i + size):
            for col in range(j, j + size):
                grid[row][col] = value

    def tileGrid(self, grid, n, m, currentMinSquares):
        # n is the number of rows
        # m is the number of cols

        # if the path we're exploring is already equal to or more than the min we found so far
        # then there's no need to keep exploring this path because its result will be at least
        # as good as what we found already
        if self.minNbOfTiles > currentMinSquares:
            # we need to find the next available cell to fill a square in it
            i, j = self.findNextCell(grid, n, m)

            if i is not None and j is not None:
                # we find the maximum number size square we can fit in this cell
                maxSizeSquare = self.findMaxSquare(grid, n, m, i, j)

                # we need to fill the cell with all possible square sizes ranging from 1 to maxSizeSquare
                # that way we'd be covering all our options
                for size in range(maxSizeSquare, 0, -1):
                    self.fillSquare(grid, i, j, size, True)

                    # we add +1 to currentMinSquares because we just placed a tile in the grid
                    self.tileGrid(grid, n, m, currentMinSquares + 1)

                    # when we are done exploring the above size option, we backtrack to try another size
                    self.fillSquare(grid, i, j, size, False)
            else:
                # we are done with filling the entire grid, so we need to check our current min squares
                # value against the global min squares value
                self.minNbOfTiles = min(self.minNbOfTiles, currentMinSquares)

    def tilingRectangle(self, n: int, m: int) -> int:
        # we have an n x m grid that we need to fill with squares
        # we will start with a cell and try to fit all possible size squares in it before
        # we move on to the next available cell to do the same. Each time we keep track of the
        # resulting number of squares to only memorize the result with least number of squares.
        grid = [[]] * n

        # a cell[i][j] is False means that this cell is not yet part of a square. True means that it is.
        for i in range(0, n):
            grid[i] = [False] * m

        # this variable will be shared across all recursive function calls to keep track of minimum
        self.minNbOfTiles = float('inf')

        self.tileGrid(grid, n, m, 0)

        return self.minNbOfTiles


print(Solution().tilingRectangle(n=2, m=3))
print(Solution().tilingRectangle(n=5, m=8))
print(Solution().tilingRectangle(n=11, m=13))
