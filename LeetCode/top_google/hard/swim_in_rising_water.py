'''
    https://leetcode.com/problems/swim-in-rising-water/

    778. Swim in Rising Water

    You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

    The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another
    4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
    You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

    Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
'''
import heapq

'''
    We will treat the matrix as a graph where each cell is a vertex and there is an undirected edge between all the adjacent cells.
    The weight of the undirected edge between vertices u and v is equal to max(u, v).
    
    We will make use of a 2D array minTime which will hold for each cell [i,j] the minimum time we need to wait to reach that cell.
    
    We will use Dijkstra's shortest path algorithm to get the correct answer of minimum wait time to reach cell [row, col] from [0,0].
'''

'''
    Accepted. Similar to path_with_minimum_effort.py.
'''


class Solution:
    def swimInWater(self, grid: [[int]]) -> int:
        n = len(grid)

        # we know that our matrix will be of size n x n
        minTime = [[]] * n

        for i in range(0, n):
            minTime[i] = [float('inf')] * n

        # we know that the minTime to reach cell (0,0) from cell (0,0) is 0
        minTime[0][0] = 0

        # first we insert out starting cell to the min priority queue
        minHeap = []

        # we put the minTime value first because we need to sorting in the heap to happen by that value
        # we also add all the cells to the heap just like we do in Dijkstra's algorithm
        for i in range(0, n):
            for j in range(0, n):
                heapq.heappush(minHeap, (minTime[i][j], (i, j)))

        # then we pop from the heap a cell at each iteration and relax its edges
        # we pop from the min heap because we want to relax the edges in order of ascending minTime value
        while len(minHeap) > 0:
            currentMinTime, (i, j) = heapq.heappop(minHeap)

            # first we check if the currentMinTime value is up-to-date
            while len(minHeap) > 0 and currentMinTime != minTime[i][j]:
                currentMinTime, (i, j) = heapq.heappop(minHeap)

            # now that we found a min cell with up-to-date min time value, we can proceed with relaxing its edges

            # the adjacent cells are: (i, j-1), (i, j+1), (i-1, j), (i+1, j)
            if j - 1 >= 0:
                # relax the edge (i, j) -> (i, j-1)
                edgeWeight = max(grid[i][j], grid[i][j - 1])

                oldValue = minTime[i][j - 1]

                minTime[i][j - 1] = min(minTime[i][j - 1], max(edgeWeight, minTime[i][j]))

                if minTime[i][j - 1] != oldValue:
                    # then we need to push this new value to the heap to make sure that we process it later
                    heapq.heappush(minHeap, (minTime[i][j - 1], (i, j - 1)))

            if j + 1 < n:
                # relax the edge (i, j) -> (i, j+1)
                edgeWeight = max(grid[i][j], grid[i][j + 1])

                oldValue = minTime[i][j + 1]

                minTime[i][j + 1] = min(minTime[i][j + 1], max(edgeWeight, minTime[i][j]))

                if minTime[i][j + 1] != oldValue:
                    # then we need to push this new value to the heap to make sure that we process it later
                    heapq.heappush(minHeap, (minTime[i][j + 1], (i, j + 1)))

            if i - 1 >= 0:
                # relax the edge (i, j) -> (i - 1, j)
                edgeWeight = max(grid[i][j], grid[i - 1][j])

                oldValue = minTime[i - 1][j]

                minTime[i - 1][j] = min(minTime[i - 1][j], max(edgeWeight, minTime[i][j]))

                if minTime[i - 1][j] != oldValue:
                    # then we need to push this new value to the heap to make sure that we process it later
                    heapq.heappush(minHeap, (minTime[i - 1][j], (i - 1, j)))

            if i + 1 < n:
                # relax the edge (i, j) -> (i + 1, j)
                edgeWeight = max(grid[i][j], grid[i + 1][j])

                oldValue = minTime[i + 1][j]

                minTime[i + 1][j] = min(minTime[i + 1][j], max(edgeWeight, minTime[i][j]))

                if minTime[i + 1][j] != oldValue:
                    # then we need to push this new value to the heap to make sure that we process it later
                    heapq.heappush(minHeap, (minTime[i + 1][j], (i + 1, j)))

        # when dijkstra's algorithm is done, we know that in minTime, we have the min time to each any cell from (0,0)
        # in particular, we have the min time to reach cell [n-1][n-1]
        return minTime[n - 1][n - 1]


print(Solution().swimInWater([[0, 2], [1, 3]]))
print(Solution().swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
print(Solution().swimInWater([[1]]))
