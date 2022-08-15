class Solution:
    def removeCoveredIntervals(self, intervals: [[int]]) -> int:
        def doesCover(firstRange, secondRange):
            return secondRange[0] <= firstRange[0] and firstRange[1] <= secondRange[1]


        isValid = [True] * len(intervals)  # isValid = [True, True, True]

        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))  # intervals = (1,6) (7, 9) (12, 15)

        for i in range(0, len(intervals)):
            for j in range(0, i):
                if isValid[j] and doesCover(intervals[i], intervals[j]):
                    isValid[i] = False
                    break

            if isValid[i]:
                for j in range(i + 1, len(intervals)):
                    if intervals[j][0] == intervals[i][0]:
                        if isValid[j] and doesCover(intervals[i], intervals[j]):
                            isValid[i] = False
                            break
                    else:
                        break

        return sum(isValid)