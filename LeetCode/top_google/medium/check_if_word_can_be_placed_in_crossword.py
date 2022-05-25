'''
    https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

    2018. Check if Word Can Be Placed In Crossword

    You are given an m x n matrix board, representing the current state of a crossword puzzle.
    The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

    A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:
        - It does not occupy a cell containing the character '#'.
        - The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
        - There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
        - There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.

    Given a string word, return true if word can be placed in board, or false otherwise.
'''

'''
    Correct but TLE => we need to memorize some solutions to reduce computations for others.
    
    Potentially useful:
        Also, another observation: down(word) = up(reverse(word)).
        Also, another observation: right(word) = left(reverse(word)).
    
    Just to reduce the amount of code used maybe?
'''


class Solution:
    def placeUp(self, board, word, i, j, m, n):
        # try to go up => the variable is the row and it decreases
        k = i - 1  # we already placed the first letter at board[i][j] so k (row variable) starts at i-1
        c = 1  # we already placed the first letter of word so c starts at 1

        while k >= 0 and c < len(word):
            # we try to place each letter
            if (board[k][j] != '#') and (board[k][j] == ' ' or board[k][j] == word[c]):
                c += 1
                k -= 1
            else:
                # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c])
                break

        # we are here for one of three reasons
        # 1) k < 0 => reached end of board
        # 2) c >= len(word) => reached end of word
        # 3) board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c]) => unable to place word in this direction

        # case 1:
        if k < 0 or c >= len(word):
            # check if the word was placed => c == len(word)
            # AND the cell right before the word is either a block or end of board
            # AND the cell after it is either block or end of board
            return c == len(word) and (i + 1 >= m or board[i + 1][j] == '#') and (i - len(word) < 0 or board[i - len(word)] == '#')
        else:
            # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c]) => unable to place word in this direction
            return False

    def placeDown(self, board, word, i, j, m, n):
        # try to go down => the variable is the row and it increases
        k = i + 1  # we already placed the first letter at board[i][j] so k (row variable) starts at i+1
        c = 1  # we already placed the first letter of word so c starts at 1

        while k < m and c < len(word):
            # we try to place each letter
            if (board[k][j] != '#') and (board[k][j] == ' ' or board[k][j] == word[c]):
                c += 1
                k += 1
            else:
                # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c])
                break

        # we are here for one of three reasons
        # 1) k >= m => reached end of board
        # 2) c >= len(word) => reached end of word
        # 3) board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c]) => unable to place word in this direction

        # case 1:
        if k >= m or c >= len(word):
            # check if the word was placed => c == len(word)
            # AND the cell right before the word is either a block or end of board
            # AND the cell after it is either block or end of board
            return c == len(word) and (i - 1 < 0 or board[i - 1][j] == '#') and (i + len(word) >= m or board[i + len(word)][j] == '#')
        else:
            # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c]) => unable to place word in this direction
            return False

    def placeRight(self, board, word, i, j, m, n):
        # try to go right => the variable is the col and it increases
        h = j + 1  # we already placed the first letter at board[i][j] so h (col variable) starts at j+1
        c = 1  # we already placed the first letter of word so c starts at 1

        while h < n and c < len(word):
            # we try to place each letter
            if (board[i][h] != '#') and (board[i][h] == ' ' or board[i][h] == word[c]):
                c += 1
                h += 1
            else:
                # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c])
                break

        # we are here for one of three reasons
        # 1) h >= n => reached end of board
        # 2) c >= len(word) => reached end of word
        # 3) board[i][h] == '#' OR (board[i][h] != ' ' AND board[i][h] != word[c]) => unable to place word in this direction

        # case 1:
        if h >= n or c >= len(word):
            # check if the word was placed => c == len(word)
            # AND the cell right before the word is either a block or end of board
            # AND the cell after it is either block or end of board
            return c == len(word) and (j - 1 < 0 or board[i][j - 1] == '#') and (j + len(word) >= n or board[i][j + len(word)] == '#')
        else:
            # board[i][h] == '#' OR (board[i][h] != ' ' AND board[i][h] != word[c]) => unable to place word in this direction
            return False

    def placeLeft(self, board, word, i, j, m, n):
        # try to go left => the variable is the col and it decreases
        h = j - 1  # we already placed the first letter at board[i][j] so h (col variable) starts at j - 1
        c = 1  # we already placed the first letter of word so c starts at 1

        while h >= 0 and c < len(word):
            # we try to place each letter
            if (board[i][h] != '#') and (board[i][h] == ' ' or board[i][h] == word[c]):
                c += 1
                h -= 1
            else:
                # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c])
                break

        # we are here for one of three reasons
        # 1) h < 0 => reached end of board
        # 2) c >= len(word) => reached end of word
        # 3) board[i][h] == '#' OR (board[i][h] != ' ' AND board[i][h] != word[c]) => unable to place word in this direction

        # case 1:
        if h < 0 or c >= len(word):
            # check if the word was placed => c == len(word)
            # AND the cell right before the word is either a block or end of board
            # AND the cell after it is either block or end of board
            return c == len(word) and (j + 1 >= n or board[i][j + 1] == '#') and (j - len(word) < 0 or board[i][j - len(word)] == '#')
        else:
            # board[i][h] == '#' OR (board[i][h] != ' ' AND board[i][h] != word[c]) => unable to place word in this direction
            return False

    def placeWordInCrossword(self, board: [[str]], word: str) -> bool:
        m = len(board)  # number of rows
        n = len(board[0])  # number of cols => safe to do this because 1 <= m,n

        for i in range(0, m):
            # at each cell in this row, we try to place the first letter of word
            for j in range(0, n):
                # a cell [i][j] is valid to start placing the word if:
                # (board[i][j] is empty OR board[i][j] == word[0]) AND board[i][j] != "#"
                if (board[i][j] != '#') and (board[i][j] == ' ' or board[i][j] == word[0]):
                    # we can try to place the word by going up or down (vertically) OR left or right (horizontally)
                    if self.placeUp(board, word, i, j, m, n):
                        return True

                    if self.placeRight(board, word, i, j, m, n):
                        return True

                    if self.placeDown(board, word, i, j, m, n):
                        return True

                    if self.placeLeft(board, word, i, j, m, n):
                        return True

        return False


'''
    In the below solution, we have:
    - down[i][j] = False if there's no way to place word at board[i][j] downward
    - up[i][j] = False if there's no way to place word at board [i][j] upward
    - right[i][j] = False if there's no way to place word at board [i][j] to the right
    - left[i][j] = False if there's no way to place word at board [i][j] to the left
    
    We will then infer:
    - if board[i-1][j] != '#' and down[i-1][j] == False => down[i][j] = False
    - if board[i][j-1] != '#' and right[i][j-1] == False => right[i][j] = False
    - if board[i+1][j] != '#' and up[i+1][j] == False => up[i][j] = False
    - if board[i][j+1] != '#' and left[i][j+1] == False => left[i][j] = False
    
    We will focus on down and right because they index precomputed results.
'''


class Solution2:
    def placeUp(self, board, word, i, j, m, n):
        # try to go up => the variable is the row and it decreases
        k = i - 1  # we already placed the first letter at board[i][j] so k (row variable) starts at i-1
        c = 1  # we already placed the first letter of word so c starts at 1

        while k >= 0 and c < len(word):
            # we try to place each letter
            if (board[k][j] != '#') and (board[k][j] == ' ' or board[k][j] == word[c]):
                c += 1
                k -= 1
            else:
                # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c])
                break

        # we are here for one of three reasons
        # 1) k < 0 => reached end of board
        # 2) c >= len(word) => reached end of word
        # 3) board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c]) => unable to place word in this direction

        # case 1:
        if k < 0 or c >= len(word):
            # check if the word was placed => c == len(word)
            # AND the cell right before the word is either a block or end of board
            # AND the cell after it is either block or end of board
            return c == len(word) and (i + 1 >= m or board[i + 1][j] == '#') and (i - len(word) < 0 or board[i - len(word)] == '#')
        else:
            # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c]) => unable to place word in this direction
            return False

    def placeDown(self, board, word, i, j, m, n):
        # try to go down => the variable is the row and it increases
        k = i + 1  # we already placed the first letter at board[i][j] so k (row variable) starts at i+1
        c = 1  # we already placed the first letter of word so c starts at 1

        while k < m and c < len(word):
            # we try to place each letter
            if (board[k][j] != '#') and (board[k][j] == ' ' or board[k][j] == word[c]):
                c += 1
                k += 1
            else:
                # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c])
                break

        # we are here for one of three reasons
        # 1) k >= m => reached end of board
        # 2) c >= len(word) => reached end of word
        # 3) board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c]) => unable to place word in this direction

        # case 1:
        if k >= m or c >= len(word):
            # check if the word was placed => c == len(word)
            # AND the cell right before the word is either a block or end of board
            # AND the cell after it is either block or end of board
            return c == len(word) and (i - 1 < 0 or board[i - 1][j] == '#') and (i + len(word) >= m or board[i + len(word)][j] == '#')
        else:
            # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c]) => unable to place word in this direction
            return False

    def placeRight(self, board, word, i, j, m, n):
        # try to go right => the variable is the col and it increases
        h = j + 1  # we already placed the first letter at board[i][j] so h (col variable) starts at j+1
        c = 1  # we already placed the first letter of word so c starts at 1

        while h < n and c < len(word):
            # we try to place each letter
            if (board[i][h] != '#') and (board[i][h] == ' ' or board[i][h] == word[c]):
                c += 1
                h += 1
            else:
                # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c])
                break

        # we are here for one of three reasons
        # 1) h >= n => reached end of board
        # 2) c >= len(word) => reached end of word
        # 3) board[i][h] == '#' OR (board[i][h] != ' ' AND board[i][h] != word[c]) => unable to place word in this direction

        # case 1:
        if h >= n or c >= len(word):
            # check if the word was placed => c == len(word)
            # AND the cell right before the word is either a block or end of board
            # AND the cell after it is either block or end of board
            return c == len(word) and (j - 1 < 0 or board[i][j - 1] == '#') and (j + len(word) >= n or board[i][j + len(word)] == '#')
        else:
            # board[i][h] == '#' OR (board[i][h] != ' ' AND board[i][h] != word[c]) => unable to place word in this direction
            return False

    def placeLeft(self, board, word, i, j, m, n):
        # try to go left => the variable is the col and it decreases
        h = j - 1  # we already placed the first letter at board[i][j] so h (col variable) starts at j - 1
        c = 1  # we already placed the first letter of word so c starts at 1

        while h >= 0 and c < len(word):
            # we try to place each letter
            if (board[i][h] != '#') and (board[i][h] == ' ' or board[i][h] == word[c]):
                c += 1
                h -= 1
            else:
                # board[k][j] == '#' OR (board[k][j] != ' ' AND board[k][j] != word[c])
                break

        # we are here for one of three reasons
        # 1) h < 0 => reached end of board
        # 2) c >= len(word) => reached end of word
        # 3) board[i][h] == '#' OR (board[i][h] != ' ' AND board[i][h] != word[c]) => unable to place word in this direction

        # case 1:
        if h < 0 or c >= len(word):
            # check if the word was placed => c == len(word)
            # AND the cell right before the word is either a block or end of board
            # AND the cell after it is either block or end of board
            return c == len(word) and (j + 1 >= n or board[i][j + 1] == '#') and (j - len(word) < 0 or board[i][j - len(word)] == '#')
        else:
            # board[i][h] == '#' OR (board[i][h] != ' ' AND board[i][h] != word[c]) => unable to place word in this direction
            return False

    def placeWordInCrossword(self, board: [[str]], word: str) -> bool:
        m = len(board)  # number of rows
        n = len(board[0])  # number of cols => safe to do this because 1 <= m,n

        down = [[]] * m
        right = [[]] * m

        for i in range(0, m):
            down[i] = [None] * n
            right[i] = [None] * n

        for i in range(0, m):
            # at each cell in this row, we try to place the first letter of word
            for j in range(0, n):
                # a cell [i][j] is valid to start placing the word if:
                # (board[i][j] is empty OR board[i][j] == word[0]) AND board[i][j] != "#"
                if (board[i][j] != '#') and (board[i][j] == ' ' or board[i][j] == word[0]):
                    # we can try to place the word by going up or down (vertically) OR left or right (horizontally)

                    # to place the word upward, we need enough space vertically. So, i - len(word) >= -1.
                    if i - len(word) >= -1 and self.placeUp(board, word, i, j, m, n):
                        return True

                    # to place the word to the right, we need enough space horizontally. So, j + len(word) <= n.
                    if j + len(word) <= n:
                        # check if we can directly infer the result of this attempt from memo
                        # if board[i][j - 1] != '#' and right[i][j - 1] == False = > right[i][j] = False
                        if board[i][j - 1] != '#' and right[i][j - 1] == False:
                            right[i][j] = False
                        else:
                            if self.placeRight(board, word, i, j, m, n):
                                return True
                            else:
                                right[i][j] = False

                    # to place the word downward, we need enough space vertically. So, i + len(word) <= m.
                    if i + len(word) <= m:
                        # check if we can directly infer the result of this attempt from memo
                        # if board[i-1][j] != '#' and down[i-1][j] == False => down[i][j] = False
                        if i - 1 >= 0 and board[i - 1][j] != '#' and down[i - 1][j] == False:
                            down[i][j] = False
                        else:
                            if self.placeDown(board, word, i, j, m, n):
                                return True
                            else:
                                down[i][j] = False

                    # to place the word to the left, we need enough space horizontally. So, j - len(word) >= -1.
                    if j - len(word) >= -1 and self.placeLeft(board, word, i, j, m, n):
                        return True

        return False


'''
    Focus on:
    
    Potentially useful:
        Also, another observation: down(word) = up(reverse(word)).
        Also, another observation: right(word) = left(reverse(word)).
        
    The trick was to make sure all conditions are satisfied (1, 2 and 3) before 
    proceeding with placing the letters of the word into board => i.e. the for loop
'''


class Solution3:
    def attemptPlaceWord(self, board, word, i, j, m, n):
        # we need to attempt to place the word downward and to the right

        # to be able to place the word downward we need 4 conditions:
        # 1) we need enough space to place the word downward: i + len(word) <= m
        # 2) we need the cell right before our word to be either end of board or #
        # 3) we need the cell right after our word to be either end of board or #
        # 4) we need all the characters from board[i][j] to board[i + len(word) - 1][j] to match word

        downwardSuccess = True

        # conditions 1, 2 and 3
        if (i + len(word) <= m) and ((i + len(word) == m) or (board[i + len(word)][j] == '#')) and ((i - 1 < 0) or board[i - 1][j] == '#'):
            c = 0  # loop over word
            row = i  # loop over rows

            # we don't have to test for row < m because we know from condition 1 that max of row is <= len(word)
            while c < len(word):
                # condition 4
                if board[row][j] == word[c] or board[row][j] == ' ':
                    c += 1
                    row += 1
                else:
                    downwardSuccess = False

                    break
        else:
            downwardSuccess = False

        # if we were able to place the word downward then we should immediately return our success result
        if downwardSuccess:
            return downwardSuccess

        # to be able to place the word to the right we need 2 conditions:
        # 1) we need enough space to place the word to the right: j + len(word) <= n
        # 2) we need the cell right before our word to be either end of board or #
        # 3) we need the cell right after our word to be either end of board or #
        # 4) we need all the characters from board[i][j] to board[i][j + len(word) - 1] to match word

        rightSuccess = True

        # conditions 1, 2 and 3
        if (j + len(word) <= n) and ((j + len(word) == n) or (board[i][j + len(word)] == '#')) and ((j - 1 < 0) or (board[i][j - 1] == '#')):
            c = 0  # loop over word
            col = j  # loop over cols

            # we don't have to test for col < n because we know from condition 1 that max of col is <= len(word)
            while c < len(word):
                # condition 4
                if board[i][col] == word[c] or board[i][col] == ' ':
                    c += 1
                    col += 1
                else:
                    rightSuccess = False

                    break
        else:
            rightSuccess = False

        return rightSuccess

    def placeWordInCrossword(self, board: [[str]], word: str) -> bool:
        m = len(board)  # number of rows
        n = len(board[0])  # number of cols

        # when we go down as rword, it's like coming up from below
        rword = word[::-1]

        for i in range(0, m):
            for j in range(0, n):
                # we can only start placing the word at [i][j] if the cell is not a block
                if board[i][j] != '#':
                    # now we attempt to place the word in all directions
                    if self.attemptPlaceWord(board, word, i, j, m, n) or self.attemptPlaceWord(board, rword, i, j, m, n):
                        return True

        return False


print(Solution3().placeWordInCrossword(board=[["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word="abc"))
print(Solution3().placeWordInCrossword(board=[[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word="ac"))
print(Solution3().placeWordInCrossword(board=[["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word="ca"))
