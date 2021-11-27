from sys import stdin
import math

while True:
    try:
        N_str = input()

        N = int(N_str)

        number_length = len(N_str) + 1

        left = 0

        while(True):
            left = math.log(N, 2) + number_length * math.log(10, 2)
            right = math.log(N+1, 2) + number_length * math.log(10, 2)

            if int(left) < int(right):
                break

            number_length += 1

        print(math.ceil(left))

    except EOFError:
        break

# https://github.com/morris821028/UVa/blob/master/volume007/701%20-%20The%20Archeologists'%20Dilemma.cpp
# https://www.programmersought.com/article/63602134089/