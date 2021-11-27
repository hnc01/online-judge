from sys import stdin, stdout


def attempt_solution(fragments, required_output):
    number_of_matches = 0

    for i in range(0, len(fragments)):
        for j in range(0, len(fragments)):
            if i != j and (fragments[i] + fragments[j] == required_output or fragments[j] + fragments[i] == required_output):
                fragments[i] = "x"
                fragments[j] = "x"
                number_of_matches += 1

                break

    return number_of_matches == (len(fragments) / 2)


def get_output_length(fragments):
    min = 1000
    max = 0

    for fragment in fragments:
        if len(fragment) < min:
            min = len(fragment)

        if len(fragment) > max:
            max = len(fragment)

    return min + max
    # total_files = len(fragments) / 2
    # total_bits = 0
    #
    # for fragment in fragments:
    #     total_bits += len(fragment)
    #
    # return total_bits / total_files


def solve(fragments, possible_outputs):
    for possible_output in possible_outputs:
        if attempt_solution(fragments.copy(), possible_output):
            return possible_output


def possible_solutions(fragments, output_length):
    possible_outputs = []

    for i in range(0, len(fragments)):
        first_piece = fragments[i]

        for j in range(0, len(fragments)):
            if i != j:
                second_piece = fragments[j]

                current_output = first_piece + second_piece

                if len(current_output) == output_length:
                    if current_output not in possible_outputs:
                        possible_outputs.append(current_output)

    return possible_outputs


# when we get all fragments we can do / 2 = this will give us the total number of fragments
# if we do total bits in fragments / total fragments = we get the length of the output string
# then we can concatenate all the fragments that produce the number of bits in the output we need

while True:
    try:
        cases = int(input())

        # skipping blank line
        # input()

        for case in range(0, cases):
            if case == 0:
                stdin.readline()

            fragments = []

            line = input().strip()

            while line != "":
                fragments.append(line)

                line = stdin.readline().strip()

            output_length = int(get_output_length(fragments))

            possible_outputs = possible_solutions(fragments, output_length)

            solution = solve(fragments, possible_outputs)

            stdout.write(solution + "\n")

            if case < cases - 1:
                stdout.write("\n")
        break
    except EOFError:
        break
