from sys import stdin


def count_carries(first_operand, second_operand):
    carry_count = 0
    remainder = 0

    while first_operand != 0 and second_operand != 0:
        first_operand_last_digit = first_operand % 10
        second_operand_last_digit = second_operand % 10

        digit_sum = first_operand_last_digit + second_operand_last_digit + remainder

        if digit_sum >= 10:
            # we have a carry
            carry_count += 1

            # we need to add 1 to the next sum
            remainder = 1
        else:
            remainder = 0

        first_operand = int(first_operand / 10)
        second_operand = int(second_operand / 10)

    # we might have leftover for one of the operands
    if remainder > 0:
        while first_operand != 0:
            # some digits are left here
            first_operand_last_digit = first_operand % 10

            digit_sum = first_operand_last_digit + remainder

            if digit_sum >= 10:
                carry_count += 1
                remainder = 1
            else:
                break

            first_operand = int(first_operand / 10)

        while second_operand != 0:
            # some digits are left here
            second_operand_last_digit = second_operand % 10

            digit_sum = second_operand_last_digit + remainder

            if digit_sum >= 10:
                carry_count += 1
                remainder = 1
            else:
                break

            second_operand = int(second_operand / 10)

    return carry_count


while True:
    try:
        line = stdin.readline().strip()

        while line != "0 0":
            line_array = line.split(" ")

            first_operand = int(line_array[0])
            second_operand = int(line_array[1])

            carry_count = count_carries(first_operand, second_operand)

            if carry_count == 0:
                print("No carry operation.")
            elif carry_count == 1:
                print("1 carry operation.")
            else:
                print(str(carry_count) + " carry operations.")

            line = stdin.readline().strip()

        break
    except EOFError:
        break
