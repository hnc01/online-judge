'''
    https://leetcode.com/problems/rotate-image/

    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

'''
    Accepted
'''


class Solution:
    def shift_once(self, matrix, left_boundary, right_boundary, start_cell):
        # the start direction is always right
        direction = "right"

        current_row = start_cell[0]
        current_col = start_cell[1]

        next_element = matrix[current_row][current_col]

        while True:
            if direction == "right":
                if current_col + 1 < right_boundary:
                    # we can move the current element to the right
                    temp = matrix[current_row][current_col + 1]
                    matrix[current_row][current_col + 1] = next_element
                    next_element = temp

                    current_col += 1
                elif current_row + 1 < right_boundary:
                    # we can't move to the right anymore, next direction is going down
                    direction = "down"

            elif direction == "down":
                if current_row + 1 < right_boundary:
                    temp = matrix[current_row + 1][current_col]
                    matrix[current_row + 1][current_col] = next_element
                    next_element = temp

                    current_row += 1
                elif current_col - 1 >= 0:
                    # we can't go down anymore because we reached the end of the column
                    # we need to go left now
                    direction = "left"

            elif direction == "left":
                if current_col - 1 >= left_boundary:
                    # we stay in the same row but we decrease the column
                    temp = matrix[current_row][current_col - 1]
                    matrix[current_row][current_col - 1] = next_element
                    next_element = temp

                    current_col -= 1
                elif current_row - 1 >= left_boundary:
                    # we can't go to the left anymore so we need to go up
                    direction = "up"
            elif direction == "up":
                if current_row - 1 >= left_boundary:
                    temp = matrix[current_row - 1][current_col]
                    matrix[current_row - 1][current_col] = next_element
                    next_element = temp

                    current_row -= 1
                else:
                    # if we can't go up anymore then we're done with rotating this outer square
                    break

    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start_row = 0
        start_col = 0

        # always have at least one row in the matrix
        matrix_length = len(matrix[0])

        while matrix_length > 0:
            for i in range(0, matrix_length - 1):
                # set start and end boundaries because we don't always at matrix_length and 0
                # with each iteration move every element to the next slot
                self.shift_once(matrix, start_col, start_col + matrix_length, (start_row, start_col))

            start_col += 1
            start_row += 1
            matrix_length -= 2


matrix = []

matrix.append([1, 2])
matrix.append([3, 4])

Solution().rotate(matrix)

print(matrix)
