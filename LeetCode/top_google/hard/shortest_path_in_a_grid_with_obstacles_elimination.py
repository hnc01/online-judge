'''
    https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

    1293. Shortest Path in a Grid with Obstacles Elimination

    You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
    You can move up, down, left, or right from and to an empty cell in one step.

    Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1)
    given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
'''
import heapq
import math

'''
    the below is correct but TLE. Maybe we need to memorize the shortest path for cells we've already seen so
    we don't have to recompute?
'''


class Solution:
    def shortestPathHelper(self, grid, k, rows, cols, i, j, visited):
        if i == rows - 1 and j == cols - 1:
            # we reached the last cell so no more paths to discover => cost here is 0
            return 0
        else:
            # we haven't reached our destination so we need to keep looking

            # we mark the current cell as visited
            visited.add((i, j))

            minPath = float('inf')

            # our possible moves are up, down, left and right
            # up = (i-1, j) | down = (i+1, j) | right = (i, j+1) | left = (i, j-1)
            directions = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]

            for direction in directions:
                if direction[0] >= 0 and direction[0] < rows and direction[1] >= 0 and direction[1] < cols and direction not in visited:
                    if grid[direction[0]][direction[1]] == 1:
                        # we have an obstacle here => let's see if we have enough k to remove it
                        if k > 0:
                            # we can explore this path by removing this obstacle
                            minPath = min(minPath, 1 + self.shortestPathHelper(grid, k - 1, rows, cols, direction[0], direction[1], visited.copy()))

                        # else we can't explore this path
                    else:
                        # we don't have an obstacle so we can explore this path
                        minPath = min(minPath, 1 + self.shortestPathHelper(grid, k, rows, cols, direction[0], direction[1], visited.copy()))

            return minPath

    def shortestPath(self, grid: [[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        minPath = self.shortestPathHelper(grid, k, rows, cols, 0, 0, set())

        if math.isinf(minPath):
            return -1

        return minPath


'''
    Use Dijkstra's shortest path with cost = (steps, k).
    
    The below leads to incorrect results because we're always going with the shortest path which might
    lead us to a dead end vs a longer path who has higher k left which could remove obstacles down the line.
'''


class Solution2:
    def shortestPath(self, grid: [[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # we will create another grid that's dp and we will explore the path from each cell.
        # We save results in each cell as we go along and use these saved results as we proceed.
        # This will be a DP approach (top-down) in each cell we will save a tuple (steps, k) which represents
        # the number of steps and k required to reach this cell.

        dp = [[]] * rows

        for i in range(0, rows):
            dp[i] = [(float('inf'), float('inf'))] * cols

        # to reach grid[0][0] we need 0 steps and 0 k => (0,0)
        dp[0][0] = (0, 0)

        # now we need min priority queue to implement dijkstra's shortest path algorithm
        minHeap = []

        for i in range(0, rows):
            for j in range(0, cols):
                heapq.heappush(minHeap, (dp[i][j], (i, j)))

        while len(minHeap) > 0:
            minPath, cell = heapq.heappop(minHeap)

            # to make sure that we have the most up-to-date value for a popped cell from queue
            while len(minHeap) > 0 and dp[cell[0]][cell[1]] != minPath:
                minPath, cell = heapq.heappop(minHeap)

            # now we relax all the edges coming out of this cell
            # the edges are up, down, right and left
            # relax algorithm is: if child.d > parent.d + 1 then child.d = parent.d + 1

            # with might exit the above while loop and still not have the up-to-date value
            # for minPath of cell because the heap is now empty and we've already process the
            # valid entries
            if dp[cell[0]][cell[1]] == minPath:
                i, j = cell[0], cell[1]

                directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

                for direction in directions:
                    if direction[0] >= 0 and direction[0] < rows and direction[1] >= 0 and direction[1] < cols:
                        # this direction is valid and within grid
                        # now we check to see if taking this step would require the consumption of a k
                        if grid[direction[0]][direction[1]] == 1:
                            # we have an obstacle so to come here we need to consume a k
                            if minPath[1] + 1 <= k:
                                # we can consume the k because we haven't exhausted it yet in this path
                                # relax the edge while consuming k
                                if dp[direction[0]][direction[1]] > (minPath[0] + 1, minPath[1] + 1):
                                    # update the min path for this child cell
                                    dp[direction[0]][direction[1]] = (minPath[0] + 1, minPath[1] + 1)

                                    # push this new value to queue
                                    heapq.heappush(minHeap, (dp[direction[0]][direction[1]], (direction[0], direction[1])))

                            # else, there's no way for us to reach this cell from this path so we don't update the value
                        else:
                            # we can safely go to this cell without consuming a k
                            # relax the edge
                            if dp[direction[0]][direction[1]] > (minPath[0] + 1, minPath[1]):
                                # update the min path for this child cell
                                dp[direction[0]][direction[1]] = (minPath[0] + 1, minPath[1])

                                # push this new value to queue
                                heapq.heappush(minHeap, (dp[direction[0]][direction[1]], (direction[0], direction[1])))

        # the min distance to reach (rows-1, cols-1) should be in dp[rows-1][cols-1]
        if not math.isinf(dp[rows - 1][cols - 1][0]):
            return dp[rows - 1][cols - 1][0]

        return -1


'''
    Another way of exploring all paths once is by doing BFS starting from top left corner.
    
    Accepted
'''

class Solution3:
    def shortestPath(self, grid: [[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # by doing BFS, we have the length of the path in the number of levels down the tree
        queue = []

        # (coordinates, steps taken, k left)
        queue.append(((0, 0), 0, k))

        # to not visited already seen cells more than once
        # not only will we save the cells we've seen but also the remaining k we've seen with them
        # that way, if we reach a cell with a different number of remaining k, we can still explore that path
        visited = set()

        while len(queue) > 0:
            cell, stepsTaken, kLeft = queue.pop(0)

            if cell == (rows-1, cols - 1):
                # we've reached our destination so we return its shortest path
                return stepsTaken

            # explore all the paths coming out of cell
            i, j = cell

            adjacency = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]

            for adjacent in adjacency:
                if adjacent[0] >= 0 and adjacent[0] < rows and adjacent[1] >= 0 and adjacent[1] < cols:
                    # this is a valid adjacent cell
                    if grid[adjacent[0]][adjacent[1]] == 1:
                        # we need to consume a k by going through this path
                        if kLeft > 0 and (adjacent, kLeft - 1) not in visited:
                            queue.append((adjacent, stepsTaken + 1, kLeft - 1))
                            # in BFS algo, whenever we see a new cell, we mark it as seen (i.e., we don't wait
                            # until all its adjacents to be processed)
                            visited.add((adjacent, kLeft - 1))

                        # else we can add this cell to our path because we can't reach it from current parent cell
                    else:
                        if (adjacent,  kLeft) not in visited:
                            queue.append((adjacent, stepsTaken + 1, kLeft))
                            # in BFS algo, whenever we see a new cell, we mark it as seen (i.e., we don't wait
                            # until all its adjacents to be processed)
                            visited.add((adjacent, kLeft))

        # we explored all the cells we can reached and we didn't return stepsTaken => we couldn't reached the bottom right corner
        return -1


print(Solution3().shortestPath(
    [
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0]]
    , 1))

print(Solution3().shortestPath(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1))
print(Solution3().shortestPath(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1))
print(Solution3().shortestPath([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 5))
print(Solution3().shortestPath(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=0))
