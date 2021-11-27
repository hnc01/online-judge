from sys import stdin, stdout
import datetime

# TODO test https://www.udebug.com/UVa/10191 "fbroom"

def merge_schedule(schedule):
    new_schedule = []

    for i in range(0, len(schedule)):
        (current_start_time, current_end_time) = schedule[i]

        if len(new_schedule) > 0:
            (previous_start_time, previous_end_time) = new_schedule[len(new_schedule) - 1]

            if current_start_time < previous_end_time or current_start_time == previous_start_time:
                # the current appointment starts during the previous appointment
                # we need to merge
                if current_end_time > previous_end_time:
                    tuple_element = list(new_schedule[len(new_schedule) - 1])
                    tuple_element[1] = current_end_time

                    new_schedule[len(new_schedule) - 1] = tuple(tuple_element)
            else:
                new_schedule.append((current_start_time, current_end_time))
        else:
            new_schedule.append((current_start_time, current_end_time))

    return new_schedule


def minute_difference(start_time, end_time):
    start_time_datetime = datetime.datetime.combine(datetime.date.today(), start_time)
    end_time_datetime = datetime.datetime.combine(datetime.date.today(), end_time)

    time_delta = end_time_datetime - start_time_datetime
    total_seconds = time_delta.total_seconds()

    minutes = total_seconds / 60

    return minutes


def find_longest_nap(schedule):
    day_start = datetime.datetime.strptime("10:00", '%H:%M').time()
    day_end = datetime.datetime.strptime("18:00", '%H:%M').time()

    nap_start_time = None
    max_nap_time = 0

    for i in range(0, len(schedule)):
        (start_time, end_time) = schedule[i]

        if i == 0 and start_time > day_start:
            # check with day_start maybe he can nap at the start of the day
            nap_time = minute_difference(day_start, start_time)

            if nap_time > max_nap_time:
                max_nap_time = nap_time
                nap_start_time = day_start

        if i == len(schedule) - 1 and end_time < day_end:
            # check with day_end maybe he can nap at the end of the day
            nap_time = minute_difference(end_time, day_end)

            if nap_time > max_nap_time:
                max_nap_time = nap_time
                nap_start_time = end_time

        # after checking if we're in the edge cases, check with current end time with next start time
        if i < len(schedule) - 1:
            (next_start_time, next_end_time) = schedule[i + 1]

            nap_time = minute_difference(end_time, next_start_time)

            if nap_time > max_nap_time:
                max_nap_time = nap_time
                nap_start_time = end_time

    return (nap_start_time, max_nap_time)


case = 1

while True:
    try:
        appointments = int(input())

        schedule = []

        for appointment in range(0, appointments):
            line = stdin.readline().strip()
            line_array = line.split(" ")

            start_time = line_array[0]
            start_time_obj = datetime.datetime.strptime(start_time, '%H:%M').time()

            end_time = line_array[1]
            end_time_obj = datetime.datetime.strptime(end_time, '%H:%M').time()

            schedule.append((start_time_obj, end_time_obj))

        if len(schedule) > 0:
            # sorted the schedule based on start_time
            schedule.sort()

            schedule = merge_schedule(schedule)

            (nap_start_time, nap_duration) = find_longest_nap(schedule)

            nap_start_time_string = ""
            nap_duration_string = ""

            if nap_duration < 60:
                nap_duration_string = str(int(nap_duration)) + " minutes"
            else:
                nap_duration_string = str(int(nap_duration // 60)) + " hours and " + str(int(nap_duration % 60)) + " minutes"

            print("Day #" + str(case) + ": the longest nap starts at " + str(nap_start_time.strftime("%H:%M")) + " and will last for " + nap_duration_string + ".")
        else:
            print("Day #" + str(case) + ": the longest nap starts at 10:00 and will last for 8 hours and 0 minutes.")

        case += 1
    except EOFError:
        break