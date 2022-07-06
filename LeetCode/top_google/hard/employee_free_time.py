'''
    https://leetcode.com/problems/employee-free-time/

    759. Employee Free Time

    We are given a list schedule of employees, which represents the working time for each employee.

    Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

    Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

    (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays.
    For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).
    Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
'''

# Definition for an Interval.
import math


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __str__(self):
        return '(' + str(self.start) + "," + str(self.end) + ')'

    def __repr__(self):
        return str(self)


'''
    Accepted
'''


class Solution:
    def isValidRange(self, startToTimestamp, limit, axisValues, rangeEnd, n):
        validTimestamps = []

        for i in range(0, limit + 1):
            if axisValues[i] in startToTimestamp:
                validTimestamps.extend(startToTimestamp[axisValues[i]])

        # then out of all the valid timestamps, we choose only the ones >= rangeEnd
        validTimestampsCount = 0

        for endValue in validTimestamps:
            if endValue >= rangeEnd:
                validTimestampsCount += 1

        return validTimestampsCount == n

    def employeeFreeTime(self, schedule: [[Interval]]) -> [Interval]:
        # first, we generate for every employee the intervals of their free times
        # n is the total number of employees
        n = len(schedule)

        # the unique time values that we have so we can study intersections only in available ranges
        axisValues = set()

        startToTimestamp = {}

        for i in range(0, n):
            employeeSchedule = schedule[i]

            intervalStart = float('-inf')

            for j in range(0, len(employeeSchedule)):
                if intervalStart not in startToTimestamp:
                    startToTimestamp[intervalStart] = []

                startToTimestamp[intervalStart].append(employeeSchedule[j].start)

                axisValues.add(employeeSchedule[j].start)
                axisValues.add(intervalStart)

                intervalStart = employeeSchedule[j].end

            axisValues.add(float('inf'))
            axisValues.add(intervalStart)

            if intervalStart not in startToTimestamp:
                startToTimestamp[intervalStart] = []

            startToTimestamp[intervalStart].append(float('inf'))

        # now we sort the axisValues to make sure we're processing the data in ascending order
        axisValues = list(axisValues)
        axisValues.sort()

        validRanges = set()

        # now we go through the ranges with start = i and end = i + 1
        # each time, we find all the timestamps that start before `start` and end after `end`
        # if we find the number of such timestamps == employees => valid interval, otherwise it's invalid so ignore
        for i in range(0, len(axisValues)):
            if i + 1 < len(axisValues):
                rangeStart = axisValues[i]
                rangeEnd = axisValues[i + 1]

                # we don't care about ranges that have inf in them
                if not math.isinf(rangeStart) and not math.isinf(rangeEnd):
                    isValidRange = self.isValidRange(startToTimestamp, i, axisValues, rangeEnd, n)

                    if isValidRange:
                        validRanges.add((rangeStart, rangeEnd))

        commonFreeTimes = list(validRanges)
        commonFreeTimes.sort()

        result = []

        for start, end in commonFreeTimes:
            result.append(Interval(start, end))

        return result


i1 = Interval(1, 2)
i2 = Interval(6, 7)
i3 = Interval(3, 4)
i4 = Interval(3, 5)
i5 = Interval(9, 12)

print(Solution().employeeFreeTime(schedule=[[i1, i2], [i3], [i4, i5]]))
# print(Solution().employeeFreeTime(schedule=[[[1,2],[6,7]],[[3,4]],[[3,5],[9,12]]]))
