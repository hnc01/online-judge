while True:
    try:
        a = input()
        b = input()

        list_a = list(a)
        list_b = list(b)

        common_letters = []

        for c in list_a:
            if c in list_b:
                list_b.remove(c)
                common_letters.append(c)

        common_letters.sort()

        print("".join(common_letters))
    except EOFError:
        break
