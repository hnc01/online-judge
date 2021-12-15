'''
    https://leetcode.com/problems/merge-intervals/

    Given an array of intervals where intervals[i] = [starti, endi],
    merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

'''
    Accepted
'''


class Solution:
    def is_overlap(self, interval1, interval2):
        # overlapping interval options:
        # they overlap at one of the boundaries
        # OR one of the interval completely contains the other interval
        # we sort the intervals by start date in asc order and there's overlap when:
        # sd2 <= ed1

        # make sure that interval1 is the one with smallest start_date
        if interval2[0] < interval1[0]:
            temp = interval2
            interval2 = interval1
            interval1 = temp

        ed1 = interval1[1]
        sd2 = interval2[0]

        return sd2 <= ed1

    def merge(self, intervals: [[int]]) -> [[int]]:
        results = []

        for interval in intervals:
            temp_results = []

            new_interval = interval

            # check if this interval is in any of the intervals we already have
            for res in results:
                if self.is_overlap(res, new_interval):
                    # we need to merge these 2 intervals
                    new_interval = [int(min(res[0], new_interval[0])), int(max(res[1], new_interval[1]))]
                else:
                    temp_results.append(res)

            # finally add new interval to temp_results
            # this works if there were merges because we'd be adding the merged interval here
            # and it works when there are no merges because we'd be adding the new discovered interval here
            temp_results.append(new_interval)

            results = temp_results.copy()

        return results


print(Solution().merge([[4, 5], [1, 4]]))
