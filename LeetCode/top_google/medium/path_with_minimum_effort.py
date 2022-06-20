'''
    https://leetcode.com/problems/path-with-minimum-effort/

    1631. Path With Minimum Effort

    You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
    where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0),
    and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left,
    or right, and you wish to find a route that requires the minimum effort.

    A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

    Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
'''

import heapq

'''
    Accepted
'''

class Solution:
    def minimumEffortPath(self, heights: [[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        # first we create a minEdge structure to help us with our solution
        minEdge = [[]] * rows

        for i in range(0, rows):
            minEdge[i] = [float('inf')] * cols

        # the trivial solution we have is that to reach cell[0][0] from cell[0][0] the minimum effort is 0
        minEdge[0][0] = 0

        # the goal is keep in each minEdge[i][j] the maximum edge seen on the minimum effort path
        # we use the idea of Dijkstra's algorithm where we relax every edge exactly once
        # but we will change the relax logic to better fit our needs
        # and we will keep the heap to relax the edges in the right order
        minHeap = []

        # we put in the heap each cell along with its minEdge value
        for i in range(0, rows):
            for j in range(0, cols):
                heapq.heappush(minHeap, (minEdge[i][j], (i, j)))

        while len(minHeap) > 0:
            currentMinEdge, (i, j) = heapq.heappop(minHeap)

            # it means this value is outdated so we should ignore it
            while len(minHeap) > 0 and currentMinEdge != minEdge[i][j]:
                currentMinEdge, (i, j) = heapq.heappop(minHeap)

            # for each cell we need to relax the edge between it and its adjacent cells
            # adjacent are: cells to the right, left, up and down.
            # cell to the right is j + 1
            if j + 1 < cols:
                effort = int(abs(heights[i][j] - heights[i][j + 1]))

                oldValue = minEdge[i][j + 1]
                minEdge[i][j + 1] = min(minEdge[i][j + 1], max(minEdge[i][j], effort))

                # update the heap value of this cell only if it changed
                if oldValue != minEdge[i][j + 1]:
                    heapq.heappush(minHeap, (minEdge[i][j + 1], (i, j + 1)))

            # cell to the left is j - 1
            if j - 1 >= 0:
                effort = int(abs(heights[i][j] - heights[i][j - 1]))

                oldValue = minEdge[i][j - 1]
                minEdge[i][j - 1] = min(minEdge[i][j - 1], max(minEdge[i][j], effort))

                # update the heap value of this cell only if it changed
                if oldValue != minEdge[i][j - 1]:
                    heapq.heappush(minHeap, (minEdge[i][j - 1], (i, j - 1)))

            # cell up is i - 1
            if i - 1 >= 0:
                effort = int(abs(heights[i][j] - heights[i - 1][j]))

                oldValue = minEdge[i - 1][j]
                minEdge[i - 1][j] = min(minEdge[i - 1][j], max(minEdge[i][j], effort))

                # update the heap value of this cell only if it changed
                if oldValue != minEdge[i - 1][j]:
                    heapq.heappush(minHeap, (minEdge[i - 1][j], (i - 1, j)))

            # cell down is i + 1
            if i + 1 < rows:
                effort = int(abs(heights[i][j] - heights[i + 1][j]))

                oldValue = minEdge[i + 1][j]
                minEdge[i + 1][j] = min(minEdge[i + 1][j], max(minEdge[i][j], effort))

                # update the heap value of this cell only if it changed
                if oldValue != minEdge[i + 1][j]:
                    heapq.heappush(minHeap, (minEdge[i + 1][j], (i + 1, j)))

        return minEdge[rows - 1][cols - 1]


print(Solution().minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(Solution().minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(Solution().minimumEffortPath(heights=[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
print(Solution().minimumEffortPath(heights=[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
