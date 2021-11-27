from sys import stdin


def is_palindrome(number):
    number_array = list(str(number))

    for i in range(0, int(len(number_array) / 2)):
        first_char = number_array[i]
        last_char = number_array[len(number_array) - i - 1]

        if first_char != last_char:
            return False

    return True


def reverse_number(number):
    number_array = list(str(number))

    return int("".join(reversed(number_array)))


def reverse_add(number):
    attempts = 1

    original_number = number

    reversed_number = reverse_number(original_number)

    original_number = original_number + reversed_number

    while not is_palindrome(original_number):
        reversed_number = reverse_number(original_number)

        original_number = original_number + reversed_number

        attempts += 1

    return (original_number, attempts)


while True:
    try:
        N = int(input())

        for case in range(0, N):
            number = int(input())

            (palindrome, attempts) = reverse_add(number)

            print(str(attempts) + " " + str(palindrome))
        break
    except EOFError:
        break
