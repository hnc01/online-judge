'''
    https://leetcode.com/problems/meeting-rooms-ii/

    253. Meeting Rooms II

    Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
    return the minimum number of conference rooms required.
'''

'''
    Accepted
'''
class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        # sort based on starting time in ascending order
        intervals = sorted(intervals, key= lambda x: x[0])

        # keep track of meetings that are still running (end time only?)
        ongoing_meetings = []
        meeting_rooms = 0

        for interval in intervals:
            start_time, end_time = interval[0], interval[1]

            # check if we have ongoing meetings
            if len(ongoing_meetings) > 0:
                # we have ongoing meetings and we need to see if they finished or not
                # we need to see how many of the currently running meetings have end time <= start time of current meeting
                new_ongoing_meetings = []

                for ongoing_meeting_end_time in ongoing_meetings:
                    if ongoing_meeting_end_time > start_time:
                        # the meeting is still happening and we need to cater for it
                        new_ongoing_meetings.append(ongoing_meeting_end_time)
                    # else:
                    # the meeting already ended so we don't to cater for it

                # finally we add the end time of the current meeting to the list of ongoing meetings
                new_ongoing_meetings.append(end_time)

                ongoing_meetings = new_ongoing_meetings

                # now that we have the total number of ongoing meetings at the same time, we need to see if we have
                # enough meetings rooms for them
                # if meeting_rooms >= len(ongoing_meetings):
                # then we don't have to do anything
                if meeting_rooms < len(ongoing_meetings):
                    meeting_rooms += 1
            else:
                # we don't have any ongoing meetings so we can use any of the ones we created
                # if we don't have any meeting rooms yet, then we create one
                if meeting_rooms == 0:
                    meeting_rooms += 1

                # we need to add the current meeting to the list of ongoing meetings
                ongoing_meetings.append(interval[1])

        return meeting_rooms

print(Solution().minMeetingRooms([[5, 10], [0, 30], [15, 20], [5, 10], [0, 30], [15, 20]]))
print(Solution().minMeetingRooms([[7,10],[2,4]]))
print(Solution().minMeetingRooms([[2,4]]))
