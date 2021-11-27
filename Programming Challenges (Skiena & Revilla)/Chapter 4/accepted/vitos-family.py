from sys import stdin, stdout


def compute_distance_sum(relatives_locations, vito_location):
    sum = 0

    for location in relatives_locations:
        diff = abs(vito_location - location)

        sum += diff

    return int(sum)


def get_minimal_distance_sum(relatives_locations):
    # sort the array in ascending order
    relatives_locations.sort()

    N = len(relatives_locations)

    # getting vito's optimal position
    if N % 2 != 0:
        # we have an odd number of relatives = vito in the middle
        vito_location = relatives_locations[N//2]
    else:
        # we have an even number of relatives so the middle is between the 2 middles
        vito_location = (relatives_locations[N//2] + relatives_locations[N//2 - 1]) * 0.5

    return compute_distance_sum(relatives_locations, vito_location)


while True:
    try:
        cases = int(input())

        for case in range(0, cases):
            line = stdin.readline().strip()

            # the first entry is the number of relatives
            relatives_locations = line.split(" ")

            number_of_relatives = int(relatives_locations[0])

            # removing the first entry because it's just number of relatives
            relatives_locations.pop(0)

            # turn every entry into an int
            relatives_locations = [int(x) for x in relatives_locations]

            print(get_minimal_distance_sum(relatives_locations))

        break
    except EOFError:
        break
