# This solution involves the multinational coefficient function, which is defined as follows.
# For a multinomial such as (x1 + x2 + x3 …)^n, the coefficient of the element of the product with the exponent n1 for x1,
# n2 for x2 and so on is equal n!/(n1! * n2! *n3! …).

from sys import stdin
import math

while True:
    try:
        line = stdin.readline().strip()

        if line == "":
            break

        line = line.split(" ")

        n = int(line[0])
        k = int(line[1])

        coefficients = stdin.readline().strip().split(" ")

        coefficients_product = 1

        for coeff in coefficients:
            coefficients_product *= math.factorial(int(coeff))

        print(int(math.factorial(n) / coefficients_product))

    except EOFError:
        break
