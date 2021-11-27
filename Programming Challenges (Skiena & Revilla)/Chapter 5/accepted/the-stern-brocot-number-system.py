from sys import stdin


def compare_fractions(n, m, x, y):
    if n == x and m == y:
        return 0
    elif (n * y) < (x * m):
        # (n / m) < (x / y) => n * y < x * m
        return -1
    else:
        # (n / m) > (x / y) => n * y > x * m
        return 1


# the trick here was knowing that when we go right it means we're bigger than parent
# and when we go left it means we're less than parent
while True:
    try:
        line = stdin.readline().strip()

        if line == "1 1":
            break

        line = line.split(" ")

        n = int(line[0])
        m = int(line[1])

        # 0/1
        a = 0
        b = 1

        # 1/0
        c = 1
        d = 0

        result = ""

        while True:
            x = a + c
            y = b + d

            compare_results = compare_fractions(n, m, x, y)

            if compare_results == 0:
                # we already printed the results so break
                break
            elif compare_results == -1:
                # (n/m) < (x/y) so we need to go left
                result += "L"

                # by going left we keep the same a,b (left node) but we update the right node
                c = x
                d = y
            else:
                # (n/m) > (x/y) so we need to go left
                result += "R"

                # by going right we keep the same c,d (right node) but we update the left node
                a = x
                b = y

        print(result)
    except EOFError:
        break
