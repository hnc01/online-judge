from sys import stdin, stdout
import datetime
import functools
import collections


def compare_activities(a, b):
    if a['day'] > b['day']:
        return 1
    elif a['day'] < b['day']:
        return -1
    else:
        if a['time'] > b['time']:
            return 1
        elif a['time'] == b['time']:
            return 0
        else:
            return -1


def extract_fares(line):
    fares = line.split(" ")

    fares = [int(x) for x in fares]

    return fares


def map_cars_to_activity(licenses_activities):
    cars_activities = {}

    for license_activity in licenses_activities:
        activity_array = license_activity.split(" ")

        car_license = activity_array[0]
        car_action = activity_array[2]
        car_km = activity_array[3]

        car_time = ":".join(activity_array[1].split(":")[-2:])
        car_time = datetime.datetime.strptime(car_time, '%H:%M').time()

        car_day = int(activity_array[1].split(":")[1])

        temp_car = {"action": car_action, "km": car_km, "time": car_time, "day": car_day}

        if car_license in cars_activities:
            cars_activities[car_license].append(temp_car)
        else:
            cars_activities[car_license] = [temp_car]

    return cars_activities


def merge_car_activity_pairs(cars_activities):
    car_activity_pairs = {}

    for car_license in cars_activities:
        car_activity = cars_activities[car_license]

        car_activity_details = []

        i = 0

        while i < len(car_activity) - 1:
            first_activity = car_activity[i]
            second_activity = car_activity[i + 1]

            if first_activity['action'] == "enter" and second_activity['action'] == "exit":
                km_travelled = int(abs(int(second_activity['km']) - int(first_activity['km'])))
                start_time = first_activity['time']

                temp = {"km_travelled": km_travelled, "start_time": start_time}

                car_activity_details.append(temp)

                i += 2
            else:
                i += 1

        car_activity_pairs[car_license] = car_activity_details

    return car_activity_pairs


def compute_car_bill(car_activity, fares):
    total_fare = 0

    for activity in car_activity:
        # get the house of the start time
        hour_fare = fares[int(activity['start_time'].hour)]

        activity_fare = hour_fare * activity['km_travelled']

        total_fare += activity_fare

    return total_fare


def get_licenses_bills(licenses_activities, fares):
    cars_activities = map_cars_to_activity(licenses_activities)

    # sort each license activities by time in ascending order
    for car_license in cars_activities:
        car_activity = sorted(cars_activities[car_license], key=functools.cmp_to_key(compare_activities), reverse=False)
        cars_activities[car_license] = car_activity

    car_activity_details = merge_car_activity_pairs(cars_activities)

    cars_bills = {}

    for car_license in car_activity_details:
        car_activity = car_activity_details[car_license]

        car_activity_bill = compute_car_bill(car_activity, fares)

        if car_activity_bill > 0:
            cars_bills[car_license] = (car_activity_bill / 100) + 2 + len(car_activity)

    return collections.OrderedDict(sorted(cars_bills.items()))


# travel on the road costs a certain amount per km travelled, depending on the time of day when the travel begins
# plus one dollar per trip
# plus a two dollar account charge
while True:
    try:
        cases = int(input())

        stdin.readline()

        for case in range(0, cases):
            if case != 0:
                print()

            # the fare structure
            line = input().strip()

            # mapping fares to the time of day (cents/km)
            fares = extract_fares(line)

            licenses_activities = []

            while True:
                line = stdin.readline().strip()

                if line != "":
                    licenses_activities.append(line)
                else:
                    break

            if len(licenses_activities) > 0:
                bills = get_licenses_bills(licenses_activities, fares)

                for license in bills:
                    print(license + " $" + "{:.2f}".format(bills[license]))

        break
    except EOFError:
        break
