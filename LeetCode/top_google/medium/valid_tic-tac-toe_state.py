'''
    https://leetcode.com/problems/valid-tic-tac-toe-state/

    794. Valid Tic-Tac-Toe State


    Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board
    position during the course of a valid tic-tac-toe game.

    The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

    Here are the rules of Tic-Tac-Toe:

    - Players take turns placing characters into empty squares ' '.
    - The first player always places 'X' characters, while the second player always places 'O' characters.
    - 'X' and 'O' characters are always placed into empty squares, never filled ones.
    - The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
    - The game also ends if all squares are non-empty.
    - No more moves can be played if the game is over.
'''

'''
    Accepted
'''


class Solution:
    def isWinState(self, matrix, player):
        # player wins if: matrix[0][i] = player OR matrix[1][i] = player or matrix[2][i] = player
        # player wins if: matrix[i][0] = player OR matrix[i][1] = player or matrix[i][2] = player
        # player wins if: matrix[0][0] = matrix[1][1] = matrix[2][2] = player OR matrix[0][2] = matrix[1][1] = matrix[2][0] = player
        horizontalWin = False

        for i in range(0, 3):
            # we are at row i, we need to check if the entire row is equal to player
            isWinningRow = True

            for j in range(0, 3):
                if matrix[i][j] != player:
                    # we found a cell in this row that's not equal to player
                    isWinningRow = False
                    break

            if isWinningRow:
                horizontalWin = True
                break

        if horizontalWin:
            return True

        # we don't have a horizontally, so let's check vertically
        verticalWin = False

        for j in range(0, 3):
            # we are at col j, we need to check if the entire column is equal to player
            isWinningColumn = True

            for i in range(0, 3):
                if matrix[i][j] != player:
                    # we found a cell in this row that's not equal to player
                    isWinningColumn = False
                    break

            if isWinningColumn:
                verticalWin = True
                break

        if verticalWin:
            return True

        # we don't have a horizontal win or a vertical win
        # we need to check diagonally
        diagonalWin = (matrix[0][0] == matrix[1][1] == matrix[2][2] == player) or (matrix[0][2] == matrix[1][1] == matrix[2][0] == player)

        # if diagonal win is False => we don;t have any wins so we return False
        # if diagonal win is True => we have a win so we return True
        return diagonalWin

    def validTicTacToe(self, board: [str]) -> bool:
        # matrix is a 3x3 matrix that represents board
        matrix = [[]] * 3

        oCount = 0
        xCount = 0

        for i in range(0, 3):
            currentRow = list(board[i])

            matrix[i] = []

            for cell in currentRow:
                if cell == 'X':
                    xCount += 1

                if cell == 'O':
                    oCount += 1

                matrix[i].append(cell)

        # after constructing matrix, we move on to running 3 tests on it:
        # 1) checking if both X and O are winners => it means one must have played after the one have won => return False
        # 2) checking if there's a winning state for X => if there is, then nb(X) = nb(O) + 1
        # 3) checking if there's a winning state for O => if there is, then nb(X) = nb(O)
        # 4) Since there are no winning states, check nb(X) = nb(O) OR nb(X) = nb(O) + 1

        isOWinner = self.isWinState(matrix, 'O')
        isXWinner = self.isWinState(matrix, 'X')

        # checking case (1)
        if isXWinner and isOWinner:
            return False

        # checking case (2)
        if isXWinner:
            # verify that nb(X) = nb(O) + 1
            return xCount == (oCount + 1)

        # checking case (3)
        if isOWinner:
            # verify that nb(X) = nb(O)
            return xCount == oCount

        # checking case (4)
        return (xCount == oCount) or (xCount == (oCount + 1))


print(Solution().validTicTacToe(board=["O  ", "   ", "   "]))
print(Solution().validTicTacToe(board=["XOX", " X ", "   "]))
print(Solution().validTicTacToe(board=["XOX", "O O", "XOX"]))
print(Solution().validTicTacToe(board=["OOO", "XXO", "XXX"]))
