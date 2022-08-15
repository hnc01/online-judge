class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        n = len(board)

        def checkCellValue(i, j):
            return board[i][j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        def checkValidInRow(i, j):
            for col in range(j + 1, n):
                if board[i][col] == board[i][j]:
                    return False

            return True

        def checkValidInCol(i, j):
            for row in range(i + 1, n):
                if board[row][j] == board[i][j]:
                    return False

            return True

        def checkValidSubBox(i, j):
            rowRanges = [(0, 2), (3, 5), (6, 8)]
            colRanges = [(0, 2), (3, 5), (6, 8)]

            # find the subbox for (i, j)
            rowRange, colRange = None, None

            for start, end in rowRanges:
                if start <= i <= end:
                    rowRange = (start, end)
                    break

            for start, end in colRanges:
                if start <= j <= end:
                    colRange = (start, end)
                    break

            # now check if the value in board[i][j] is in the subbox
            for r in range(rowRange[0], rowRange[1] + 1):
                for c in range(colRange[0], colRange[1] + 1):
                    if (r, c) != (i, j) and board[r][c] == board[i][j]:
                        return False

            return True

        # checks to make for each cell
        # 1: check if the value is . or 1-9. Anything else, return false.
        # we pass 1, 2: check if value is valid in the row. Else return false.
        # 3: check if value is valid in the col. Else return false.
        # 4: check if value is valid in sub-box. Else return false.
        for i in range(0, n):
            for j in range(0, n):
                if board[i][j] == '.':
                    continue

                # check 1
                if not checkCellValue(i, j):
                    return False

                # check 2
                if not checkValidInRow(i, j):
                    return False

                # check 3
                if not checkValidInCol(i, j):
                    return False

                # check 4
                if not checkValidSubBox(i, j):
                    return False

        # if we didn't return False at any point before here => valid board
        return True