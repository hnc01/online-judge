'''
    https://leetcode.com/problems/maximum-number-of-visible-points/

    1610. Maximum Number of Visible Points

    You are given an array points, an integer angle, and your location, where location = [posx, posy]
    and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

    Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate.
    In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining
    how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise.
    Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].
'''

'''
    Notes:
    - We can easily know if an angle is between 2 other angles.
    - Given 2 points (i.e., our location point and another point from points), we can calculate the angle formed by these 2 points.
    - If a point has the same coordinates as our location point, we can quickly count it as visible. 
'''
import math

'''
    Accepted
'''


class Solution:
    def visiblePoints(self, points: [[int]], angle: int, location: [int]) -> int:
        x, y = location[0], location[1]

        duplicatesCount = 0

        pointsAngles = []

        # first let's get the trivially visible points out of the way
        for point in points:
            if point[0] == x and point[1] == y:
                duplicatesCount += 1
            else:
                # this point needs to be processed later
                # calculate the angle formed by the 2 points (x,y) and current point
                # angle between 2 points is atan2(points[1] - y, points[0] - x)
                pointsAngles.append(math.atan2(point[1] - y, point[0] - x))
                # since atan2 will return our results in radians, we need to account for the angles of the form angle + 2*pi
                # we do this to make sure we're getting the angle in positive quadrant if we get it in negative quadrant when doing arctan
                pointsAngles.append(math.atan2(point[1] - y, point[0] - x) + (2 * math.pi))

        # then we sort the angles
        pointsAngles.sort()

        # since we're dealing with radians, we need to transform our angle to radian
        angle = math.radians(angle)

        highBoundary = 0

        maxCount = 0

        # now we start doing the rotations
        for lowBoundary in range(0, len(pointsAngles)):
            # we need to keep increasing highBoundary until we have the angle between high and low that's > angle
            while highBoundary < len(pointsAngles) and (pointsAngles[highBoundary] - pointsAngles[lowBoundary]) <= angle:
                highBoundary += 1

            # when we're here weh have highBoundary is 1 more element than we need so to get the number of elements between
            # high and low, we don't need to an extra +1 to the difference
            count = highBoundary - lowBoundary

            maxCount = max(maxCount, count)

        return maxCount + duplicatesCount


print(Solution().visiblePoints(points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]))
print(Solution().visiblePoints(points=[[2, 1], [2, 2], [3, 4], [1, 1]], angle=90, location=[1, 1]))
print(Solution().visiblePoints(points=[[1, 0], [2, 1]], angle=13, location=[1, 1]))
print(Solution().visiblePoints([[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]], 0, [1, 1]))
print(Solution().visiblePoints([[41, 7], [22, 94], [90, 53], [94, 54], [58, 50], [51, 96], [87, 88], [55, 98], [65, 62], [36, 47], [91, 61], [15, 41], [31, 94], [82, 80], [42, 73], [79, 6], [45, 4]],
                               17, [6, 84]))
# [26, 78], [90, 41], [94, 18], [12, 88], [42, 82], [27, 0], [85, 49], [69, 71], [13, 36], [59, 58], [58, 18], [21, 62]
print(Solution().visiblePoints([[34, 26], [35, 95], [31, 56], [84, 75], [26, 76], [22, 15]], 15, [67, 91]))
