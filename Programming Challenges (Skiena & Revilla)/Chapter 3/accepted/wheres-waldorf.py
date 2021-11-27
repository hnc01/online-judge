def find_word(word, grid):
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            # look in all directions
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

            for dir in directions:
                current_row = row
                current_col = col
                c = 0

                while grid[current_row][current_col] == word[c]:
                    current_row += dir[0]
                    current_col += dir[1]
                    c += 1

                    if c == len(word):
                        return (row + 1, col + 1)

                    if current_row < 0 or current_col < 0 or current_row >= len(grid) or current_col >= len(grid[0]):
                        break




def solve(grid, words):
    for word in words:
        result = find_word(word, grid)

        if result is not None:
            print(str(result[0]) + " " + str(result[1]))


while True:
    try:
        text = input()

        cases = int(text)

        for c in range(1, cases + 1):
            if c != 1:
                print()

            grid = []

            # skipping new line
            input()

            # contains m n
            line = input().strip().split(" ")

            m = int(line[0])
            n = int(line[1])

            for i in range(1, m + 1):
                line = input().strip()
                temp = []

                for char in line:
                    temp.append(char.lower())

                grid.append(temp)

            words_count = int(input())

            words = []

            for wc in range(1, words_count + 1):
                words.append(input().strip().lower())

            solve(grid, words)

    except EOFError:
        break
