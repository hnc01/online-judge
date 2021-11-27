from sys import stdin, stdout
import functools


def compare_jobs(a, b):
    # a[0] * b[1] doing job a before b
    # b[0] * a[1] doing job b before a
    if a[0] * b[1] > b[0] * a[1]:
        # doing a before b will cost more => a > b
        return 1
    elif a[0] * b[1] == b[0] * a[1]:
        # doesn't matter which one we do first so keep same natural order
        return 0
    else:
        # a[0] * b[1] < b[0] * a[1]:
        # doing a before b will cost less => a < b
        return -1


while True:
    try:
        cases = int(input())

        for case in range(0, cases):
            if case != 0:
                print()

            if case == 0:
                # skipping the new line between cases
                stdin.readline()

            # number of jobs 1 <= N <= 1000
            N = int(input())

            # the jobs that the shoemaker has
            jobs = []

            line = input().strip()

            index = 1

            while line != "":
                # 1 <= Ti <= 1000
                # 1 <= Si <= 10000
                (Ti, Si) = line.split(" ")

                jobs.append((int(Ti), int(Si), index))

                line = stdin.readline().strip()

                index += 1

            jobs = sorted(jobs, key=functools.cmp_to_key(compare_jobs), reverse=False)

            optimal_sequence = []

            for i in range(0, len(jobs)):
                (Ti, Si, job_index) = jobs[i]

                optimal_sequence.append(str(job_index))

            print(" ".join(optimal_sequence))

        break
    except EOFError:
        break
