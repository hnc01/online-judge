'''
    https://leetcode.com/problems/detect-squares/

    2013. Detect Squares

    You are given a stream of points on the X-Y plane. Design an algorithm that:
        - Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
        - Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
        An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

    Implement the DetectSquares class:

    - DetectSquares() Initializes the object with an empty data structure.
    - void add(int[] point) Adds a new point point = [x, y] to the data structure.
    - int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
'''

'''
    Before adding memo, it was correct by TLE. After adding memo, it got accepted.
'''


class DetectSquares:
    xCoordMap = None
    yCoordMap = None
    pointsCounts = None

    def __init__(self):
        self.xCoordMap = {}
        self.yCoordMap = {}
        self.pointsCounts = {}

    def add(self, point: [int]) -> None:
        xCoord, yCoord = point[0], point[1]

        if xCoord not in self.xCoordMap:
            self.xCoordMap[xCoord] = []

        self.xCoordMap[xCoord].append((xCoord, yCoord))

        if yCoord not in self.yCoordMap:
            self.yCoordMap[yCoord] = []

        self.yCoordMap[yCoord].append((xCoord, yCoord))

        if (xCoord, yCoord) not in self.pointsCounts:
            self.pointsCounts[(xCoord, yCoord)] = 0

        self.pointsCounts[(xCoord, yCoord)] += 1

    def count(self, point: [int]) -> int:
        xCoord, yCoord = point[0], point[1]

        # first we need to find all the points with same xCoord as the point
        # and all the points with the same yCoord as the point
        if xCoord in self.xCoordMap and yCoord in self.yCoordMap:
            xCoordPoints = self.xCoordMap[xCoord]
            yCoordPoints = self.yCoordMap[yCoord]

            # now we need to find which of the xCoordPoints and yCoordPoints are equidistant from our point
            xCoordDistances = {}
            yCoordDistances = {}

            for otherPoint in xCoordPoints:
                # the distance from (xCoord, yCoord) and a point in xCoordPoints is equal to abs(yCoord and otherYCoord)
                distance = int(abs(otherPoint[1] - yCoord))

                if distance not in xCoordDistances:
                    xCoordDistances[distance] = []

                xCoordDistances[distance].append(otherPoint)

            for otherPoint in yCoordPoints:
                # the distance from (xCoord, yCoord) and a point in yCoordPoints is equal to abs(xCoord and otherXCoord)
                distance = int(abs(otherPoint[0] - xCoord))

                if distance not in yCoordDistances:
                    yCoordDistances[distance] = []

                yCoordDistances[distance].append(otherPoint)

            # counts the total number of squares that can be formed from given point
            totalSquares = 0

            # because there could be duplicate points, maybe if we've already seen the point p1 before, we can memorize
            # its results instead of recomputing for every p2
            memo = {}

            # now that we mapped every other point to its distance from our point, we need to check all the points in xCoordDistances
            # and yCoordDistances that have same distance from our point
            for distance in xCoordDistances:
                if distance in yCoordDistances:
                    # get these pairs together and see if they can form a square
                    for p1 in xCoordDistances[distance]:
                        if p1 in memo:
                            totalSquares += memo[p1]
                        else:
                            memo[p1] = 0

                            for p2 in yCoordDistances[distance]:
                                fourthPoint = None

                                # first we need to see in which quadrant with point in its center are we attempting to create the triangle
                                if p2[0] < xCoord and p1[1] > yCoord:
                                    # quadrant 1 => look for (i-d, j+d)
                                    fourthPoint = (xCoord - distance, yCoord + distance)
                                elif p2[0] > xCoord and p1[1] > yCoord:
                                    # quadrant 2 => look for (i+d, j+d)
                                    fourthPoint = (xCoord + distance, yCoord + distance)
                                elif p2[0] > xCoord and p1[1] < yCoord:
                                    # quadrant 3 => look for (i+d, j-d)
                                    fourthPoint = (xCoord + distance, yCoord - distance)
                                elif p2[0] < xCoord and p1[1] < yCoord:
                                    # quadrant 4 => look for (i-d, j-d)
                                    fourthPoint = (xCoord - distance, yCoord - distance)

                                if fourthPoint is not None and fourthPoint in self.pointsCounts:
                                    totalSquares += self.pointsCounts[fourthPoint]
                                    memo[p1] += self.pointsCounts[fourthPoint]

            return totalSquares
        else:
            return 0


# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()

# commands = ["add", "add", "add", "count", "count", "add", "count"]
# input = [[[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]

# commands = ["count"]
# input = [[[11, 10]]]

commands = ["add", "add", "add"]
input = [[[3, 10]], [[11, 2]], [[3, 2]]]

for i in range(0, len(commands)):
    command = commands[i]

    if command == "add":
        obj.add(input[i][0])
    elif command == "count":
        print(obj.count(input[i][0]))
