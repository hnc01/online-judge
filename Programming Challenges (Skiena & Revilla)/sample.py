keyboard = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']


def map_character(char):
    if char == ' ':
        return ' '
    else:
        return keyboard[keyboard.index(char) - 1]


while True:
    try:
        text = input()

        result = ""

        for char in text:
            result += map_character(char)

        print(result)
    except EOFError:
        break
