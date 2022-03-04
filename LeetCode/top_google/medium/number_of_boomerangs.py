'''
    https://leetcode.com/problems/number-of-boomerangs/

    447. Number of Boomerangs

    You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k)
    such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

    Return the number of boomerangs.
'''
import math


class Solution:
    def numberOfBoomerangs(self, points: [[int]]) -> int:
        # first we should compute the distance between every pair of points
        # distance[coord_source] = {}
        # distances[coord_source][dist] = [] => list of points whose distance from coord_source is = dist
        distances = {}

        for i in range(0, len(points)):
            for j in range(0, len(points)):
                if i != j:
                    # calculate the distance between points[i] and points[j]
                    distance = math.dist(points[i], points[j])

                    coord_source = str(points[i][0]) + "," + str(points[i][1])
                    coord_destination = str(points[j][0]) + "," + str(points[j][1])

                    if coord_source in distances:
                        if distance in distances[coord_source]:
                            distances[coord_source][distance].append(coord_destination)
                        else:
                            distances[coord_source][distance] = [coord_destination]
                    else:
                        distances[coord_source] = {}
                        distances[coord_source][distance] = [coord_destination]

        boomerangs_count = 0

        # now distances maps each point to a set of distances and the set of points within each distance value
        # we go over each coord_source in distances and see if any of the distances it's mapped to contain more than one point
        for coord_source in distances:
            for distance in distances[coord_source]:
                if len(distances[coord_source][distance]) > 1:
                    # coord_source is mapped to more than one coord_destination with equal distance
                    # the number of resulting pairs is nPr
                    n = len(distances[coord_source][distance])
                    # because we need to permute them in pairs of 2 because the third item in the tuple is coord_source
                    r = 2

                    boomerangs_count += math.factorial(n) / math.factorial(n - r)

        return int(boomerangs_count)


# points = [[0, 0], [1, 0], [2, 0]]
# points = [[1,1],[2,2],[3,3]]
# points = [[1,1]]
# points = [[0, 0], [0, 1], [1, 0], [2, 0]]
points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]

print(Solution().numberOfBoomerangs(points))
