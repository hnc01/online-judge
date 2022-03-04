'''
    https://leetcode.com/problems/minimum-time-difference/

    539. Minimum Time Difference

    Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
'''
import datetime
import math

'''
    Accepted
'''
class Solution:
    def difference_in_minutes(self, hour1, minute1, hour2, minute2):
        first_hour = datetime.datetime.now()
        first_hour = first_hour.replace(hour=hour1, minute=minute1, second=0, microsecond=0)

        second_hour = datetime.datetime.today()
        second_hour = second_hour.replace(hour=hour2, minute=minute2, second=0, microsecond=0)

        if second_hour < first_hour:
            # first we compute the difference if we push the smaller time to the next day
            second_hour_tomorrow = second_hour + datetime.timedelta(days=1)

            min_diff_1 = int((second_hour_tomorrow - first_hour).total_seconds() / 60)

            # then we swap the first and second hour and calculate the difference
            min_diff_2 = int((first_hour - second_hour).total_seconds() / 60)

            return min(min_diff_1, min_diff_2)
        else:
            return int((second_hour - first_hour).total_seconds() / 60)

    def findMinDifference(self, timePoints: [str]) -> int:
        # first we create a list of 23 buckets and each bucket[i] will hold the minutes of all the timesPoints
        # that have hour i
        buckets = {}

        # these will map each hour bucket to its min and max minutes
        # these will allow us to calculate the time difference between 2 consecutive buckets
        min_minute = {}
        max_minute = {}

        # create a bucket for each hour 00 -> 23
        for i in range(0, 24):
            # we know that each hour will have a max of 59 minutes
            # so buckets[i] will be an array that maps each minute to its count
            # that way we don't need to sort the minutes to get the difference in minutes
            buckets[i] = [0] * 60
            min_minute[i] = float('inf')
            max_minute[i] = float('-inf')

        # we filled the buckets with the minutes
        for timePoint in timePoints:
            hour = int(timePoint.split(":")[0])
            minute = int(timePoint.split(":")[1])

            buckets[hour][minute] += 1

            min_minute[hour] = min(min_minute[hour], minute)
            max_minute[hour] = max(max_minute[hour], minute)

        min_difference = float('inf')

        # now we need to go over the data in our buckets and calculate the minute difference between all pairs of HH:MM within the same bucket
        for hour in buckets:
            minutes = buckets[hour]

            for i in range(0, len(minutes)):
                for j in range(0, len(minutes)):
                    if minutes[i] >= 1 and minutes[j] >= 1:
                        # found a sample HH:MM
                        if i == j and minutes[i] > 1:
                            # we found a duplicate HH:MM in same bucket so difference is 0
                            min_difference = min(min_difference, 0)
                        elif i != j:
                            # i != j
                            min_difference = min(min_difference, self.difference_in_minutes(hour, i, hour, j))

                # if minutes[i] == 0 it means that this minute doesn't appear in our input

        # now that we're done with the calculations that are within the same bucket, we move on to calculating
        # the minute difference between 2 consecutive buckets
        for i in range(0, len(buckets)):
            for j in range(0, len(buckets)):
                if i != j:
                    if math.isinf(min_minute[i]) or math.isinf(min_minute[j]):
                        # we need ignore combination of buckets because one doesn't have values
                        pass
                    else:
                        # now we need to compute the difference between the max of left and min of right
                        # we also need to take into consideration the difference in minutes between left_index (hour of left bucket)
                        # and right_index (hour of right bucket)
                        min_difference = min(min_difference, self.difference_in_minutes(i, max_minute[i], j, min_minute[j]))

        return int(min_difference)


# print(Solution().findMinDifference(["00:00", "23:59", "00:00"]))
# print(Solution().findMinDifference(["23:59","00:00"]))
# print(Solution().findMinDifference(["01:05","01:06", "01:58", "2:00"]))
# print(Solution().findMinDifference(["01:39","10:26","21:43"]))
print(Solution().findMinDifference(["01:01","02:01"]))
