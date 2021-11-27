import string

seed = "the quick brown fox jumps over the lazy dog"


def is_seed(line):
    if len(line) == len(seed):
        # they have the same number of character so they could be a match
        seed_list = seed.split(" ")
        line_list = line.split(" ")

        if len(seed_list) == len(line_list):
            # they have the same number of words
            for index in range(0, len(seed_list)):
                if len(seed_list[index]) != len(line_list[index]):
                    return False

            return True
        else:
            return False
    else:
        return False


def create_map(line):
    map = dict.fromkeys(string.ascii_lowercase, '')

    for index in range(0, len(line)):
        if line[index] != ' ':
            if map[line[index]] == '':
                map[line[index]] = seed[index]
            elif map[line[index]] != '' and map[line[index]] != seed[index]:
                # more than one character map to the same character
                return None

    return map


def decrypt(lines):
    for line in lines:
        if is_seed(line):
            # create the map
            map = create_map(line)

            if map is None:
                pass
            else:
                decrypted_lines = []

                for line in lines:
                    decrypted_line = ""

                    for c in line:
                        if c == ' ':
                            decrypted_line += " "
                        else:
                            if map[c] != '':
                                decrypted_line += map[c]
                            else:
                                decrypted_line = None
                                break

                    decrypted_lines.append(decrypted_line)

                if len(decrypted_lines) == len(lines) and None not in decrypted_lines:
                    for decrypted_line in decrypted_lines:
                        print(decrypted_line)

                    return

    print("No solution.")

while True:
    try:
        cases = int(input())

        # skip the new line
        input()

        for case in range(1, cases + 1):
            if case != 1:
                print()

            lines = []

            while True:
                try:
                    line = input().strip()

                    if line != "":
                        lines.append(line)
                    else:
                        break
                except EOFError:
                    break

            decrypt(lines)
    except EOFError:
        break
