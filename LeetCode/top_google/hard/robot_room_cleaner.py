'''
    https://leetcode.com/problems/robot-room-cleaner/

    489. Robot Room Cleaner

    You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where
    0 represents a wall and 1 represents an empty slot.

    The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid,
    but you can move the robot using the given API Robot.

    You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four
    given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

    When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

    Design an algorithm to clean the entire room using the following APIs:

    interface Robot {
      // returns true if next cell is open and robot moves into the cell.
      // returns false if next cell is obstacle and robot stays on the current cell.
      boolean move();

      // Robot will stay on the same cell after calling turnLeft/turnRight.
      // Each turn will be 90 degrees.
      void turnLeft();
      void turnRight();

      // Clean the current cell.
      void clean();
    }

    ** Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid
    are all surrounded by a wall. **

    Custom testing:

    The input is only given to initialize the room and the robot's position internally.
    You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned
    APIs without knowing the room layout and the initial robot's position.
'''
import random

"""
This is the robot's control interface.
You should not implement it, or speculate about its implementation
"""


class Robot:
    def __init__(self, grid, row, col):
        self.grid = grid
        self.row = row
        self.col = col
        self.m = len(grid)  # 1 <= m <= 100
        self.n = len(grid[0])  # 1 <= n <= 200
        self.direction = 'UP'

        self.isClean = [[]] * self.m

        for i in range(0, self.m):
            # initially all the cells are not clean
            self.isClean[i] = [False] * self.n

        # we mark all the wall cells as clean to avoid mistaking walls for unclean cells
        for i in range(0, self.m):
            for j in range(0, self.n):
                if self.grid[i][j] == 0:
                    self.isClean[i][j] = True

    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        if self.direction == 'UP':
            # move to (row-1, col)
            if self.row - 1 >= 0 and self.grid[self.row - 1][self.col] == 1:
                # valid move
                self.row = self.row - 1

                return True
        elif self.direction == 'RIGHT':
            # move to (row, col + 1)
            if self.col + 1 < self.n and self.grid[self.row][self.col + 1] == 1:
                # valid move
                self.col = self.col + 1

                return True
        elif self.direction == 'DOWN':
            # move to (row + 1, col)
            if self.row + 1 < self.m and self.grid[self.row + 1][self.col] == 1:
                # valid move
                self.row = self.row + 1

                return True
        else:
            # direction == LEFT
            # move to (row, col - 1)
            if self.col - 1 >= 0 and self.grid[self.row][self.col - 1] == 1:
                # valid move
                self.col = self.col - 1

                return True

        # either out of bounds or wall
        return False

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        if self.direction == 'UP':
            self.direction = 'LEFT'
        elif self.direction == 'LEFT':
            self.direction = 'DOWN'
        elif self.direction == 'DOWN':
            self.direction = 'RIGHT'
        else:
            self.direction = 'UP'

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        if self.direction == 'UP':
            self.direction = 'RIGHT'
        elif self.direction == 'RIGHT':
            self.direction = 'DOWN'
        elif self.direction == 'DOWN':
            self.direction = 'LEFT'
        else:
            self.direction = 'UP'

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        self.isClean[self.row][self.col] = True

    def isRoomClean(self):
        for i in range(0, self.m):
            for j in range(0, self.n):
                if not self.isClean[i][j]:
                    return False

        return True


'''
    - We will always visit cells in a spiral way, this will ensure that we are visiting all cells directly reachable from current cell.
    - Since we don't know where the starting cell is, we will assume it's at (0,0) and all cells will be indexed based on it.
    - For example, the cell to its left is (0, -1), the one to its right is (0, 1), the one above it is (-1, 0) and the one under it is (1, 0).
    - Since now we have indices for each cell we visited, we can keep track of the cells we've seen so far (i.e., cleaned)
    - To spiral around a cell, means going in the same direction => we'll choose going to the right always => we go up, right, down, left, up.
    - When we hit an obstacle (we either can't move to the right because there's wall or clean cell) we just go right again. After trying to go
    in all directions without any possible path, then we backtrack to earlier cells one by one and try exploring a different direction if possible.
    If we backtrack all the way to the starting cell without finding any alternative paths. It should mean we are done.
'''


class Solution:
    def backtrack(self, robot: Robot):
        # to go back means to turn around our robot and make him go in the opposite of his current direction
        # to a previous cell and reset direction to current direction
        # using turnLeft works too
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def exploreCell(self, cell: (int, int), direction: int, cleanedCells: set[int], robot: Robot):
        # direction is the index of the direction in directions => 0 is UP, 1 is RIGHT, 2 is DOWN and 3 is LEFT
        # directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        # UP => rows - 1 and col the same => (-1, 0) | RIGHT => rows the same and cols + 1 => (0, 1)
        # DOWN => rows + 1 and cols the same => (1, 0) | LEFT => rows the same and cols - 1 => (0, -1)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # we reached this cell because we know that we can move to it to clean it
        cleanedCells.add(cell)
        robot.clean()

        # now we need to spiral around it in all directions starting from given `direction`
        for i in range(0, 4):
            # this will add 1 to the direction with each iteration and circle back to start
            updatedDirection = (direction + i) % len(directions)

            # let's try to move to this cell after checking if we've already been to it
            # even if it is out of bounds, we are said to treat it like a wall and so we will
            newCell = (cell[0] + directions[updatedDirection][0], cell[1] + directions[updatedDirection][1])

            if newCell not in cleanedCells and robot.move():
                # the cell is not clean and we explore it
                # the robot already moved here so we can just go to exploring
                self.exploreCell(newCell, updatedDirection, cleanedCells, robot)

                # after we're done exploring, we backtrack to an earlier cell and try to explore the other directions
                self.backtrack(robot)

            # let the robot turn so that he can change his direction to match the index of directions array
            robot.turnRight()

        # the code will stop going into the recursion when `if newCell not in cleanedCells and robot.move():` is false
        # in every direction and so we stop making recursive calls to `exploreCell`

    def cleanRoom(self, robot: Robot):
        cleanedCells = set()  # we create a set to quickly test membership

        # we don't know which cell we're starting at so we just assume we are at (0,0) and we index everything accordingly
        startingCell = (0, 0)

        self.exploreCell(startingCell, 0, cleanedCells, robot)


robot = Robot([[1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]], 1, 3)

print(Solution().cleanRoom(robot))
print(robot.isRoomClean())
