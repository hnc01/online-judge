'''
    https://leetcode.com/problems/amount-of-new-area-painted-each-day/

    2158. Amount of New Area Painted Each Day

    There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint
    of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

    Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

    Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.
'''

'''
    Accepted
'''


class Solution:
    def isIntersect(self, firstPair, secondPair):
        # first, we make firstPair is the smallest of the pairs
        if firstPair[0] > secondPair[0]:
            firstPair, secondPair = secondPair, firstPair

        # now that we know that firstPair is the smallest of the pairs,
        # we can conclude that we have intersection IF: secondPair starts before the firstPair ends
        if secondPair[0] <= firstPair[1]:
            # need to calculate the intersection length
            # we have 2 cases: either firstPair[0] -> secondPair[0] -> firstPair[1] -> secondPair[1]
            # OR firstPair[0] -> secondPair[0] -> secondPair[1] -> firstPair[1]

            if firstPair[1] <= secondPair[1]:
                # case 1: intersection length = firstPair[1] - secondPair[0] (overlap)
                return (True, firstPair[1] - secondPair[0])
            else:
                # case 2: intersection length = secondPair[1] - secondPair[0] (complete inclusion)
                return (True, secondPair[1] - secondPair[0])
        else:
            return (False, 0)

    def amountPainted(self, paint: [[int]]) -> [int]:
        # Idea: we keep track of areas that were painted and we merge the ones that intersect
        # to keep track of the (start, end) ranges of the painted areas
        paintedAreas = []

        # to keep track of the work done everyday
        workLog = []

        for i in range(0, len(paint)):
            # check if there's an intersection between the current paint item and any of the painted areas
            intersectionAreas = []
            nonIntersectionAreas = []

            totalIntersectionLength = 0

            for paintedArea in paintedAreas:
                isIntersection, intersectionLength = self.isIntersect(paintedArea, paint[i])

                if isIntersection:
                    intersectionAreas.append(paintedArea)
                    totalIntersectionLength += intersectionLength
                else:
                    nonIntersectionAreas.append(paintedArea)

            # we know that the current day's area intersections with all the painted areas in intersectionAreas
            # and we know that there's no intersection between intersectionAreas themselves
            # we also know that paintedAreas are sorted in asc order of start => so, if there are intersections,
            # they must be following each other in order.
            totalWork = paint[i][1] - paint[i][0]

            # we need to remove from total work, all the intersections
            totalWork = totalWork - totalIntersectionLength

            workLog.append(totalWork)

            # now we need to merge intersectionAreas with the current area and add the new merged area to nonIntersectionAreas
            mergedArea = (paint[i][0], paint[i][1])

            for area in intersectionAreas:
                # merge this area with mergedArea
                mergedArea = (min(mergedArea[0], area[0]), max(mergedArea[1], area[1]))

            nonIntersectionAreas.append(mergedArea)

            paintedAreas = nonIntersectionAreas

            paintedAreas.sort(key=lambda item: (item[0], item[1]))

        return workLog


print(Solution().amountPainted(paint=[[4, 7], [1, 4], [5, 8]]))
print(Solution().amountPainted(paint=[[1, 4], [5, 8], [4, 7]]))
print(Solution().amountPainted(paint=[[1, 5], [2, 4]]))
print(Solution().amountPainted(paint=[[4, 7], [1, 4], [5, 8], [3, 6], [3, 6]]))
