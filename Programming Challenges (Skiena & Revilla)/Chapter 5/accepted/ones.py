while True:
    try:
        n = int(input())

        ones = 11
        ones_str = "11"

        while ones % n != 0:
            ones_str = ones_str + "1"
            ones = int(ones_str)

        print(len(ones_str))
    except EOFError:
        break
