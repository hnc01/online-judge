'''
    https://leetcode.com/problems/word-search/

    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
    horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

'''
    Accepted
    
    Trick:
    - We need to consider the case where there's only one element in the matrix because otherwise we'd go into the general
    case and we'd default to up = down = right = left = False which is false result overall because we have nowhere to go.
'''

class Solution:
    def exist_helper(self, board, word, m, n, row, col, visited):
        if len(word) == 0:
            return True
        elif len(word) == 1:
            return board[row][col] == word
        else:
            if board[row][col] == word[0]:
                visited_copy = visited.copy()
                visited_copy.add((row, col))

                up_direction = down_direction = right_direction = left_direction = False

                # we continue in either direction to see if we can find the rest of the word
                # up, down, left, right
                if row - 1 >= 0:
                    if (row - 1, col) not in visited_copy:
                        # we can go up
                        up_direction = self.exist_helper(board, word[1:], m, n, row - 1, col, visited_copy)

                if row + 1 < m:
                    if (row + 1, col) not in visited_copy:
                        # we can go down
                        down_direction = self.exist_helper(board, word[1:], m, n, row + 1, col, visited_copy)

                if col + 1 < n:
                    if (row, col + 1) not in visited_copy:
                        # we can go right
                        right_direction = self.exist_helper(board, word[1:], m, n, row, col + 1, visited_copy)

                if col - 1 >= 0:
                    if (row, col - 1) not in visited_copy:
                        # we can go left
                        left_direction = self.exist_helper(board, word[1:], m, n, row, col - 1, visited_copy)

                return up_direction or down_direction or right_direction or left_direction
            else:
                return False

    def exist(self, board: [[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        # we explore finding the string starting with any cell
        for row in range(0, m):
            for col in range(0, n):
                visited = set()

                if self.exist_helper(board, word, m, n, row, col, visited):
                    return True

        return False


board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"

print(Solution().exist(board, word))
