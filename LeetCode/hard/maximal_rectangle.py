'''
    https://leetcode.com/problems/maximal-rectangle/

    85. Maximal Rectangle

    Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''

'''
    Accepted time limit exceeded
'''


class Solution:
    def getMaxArea(self, matrix, i, j, rows, cols):
        max_area = float('-inf')

        # it's always the minimum col where we found matrix[row][col] == '0'
        right_boundary = cols

        # starting at cell (i,j) we keep going row by row to see the max rectangle area
        for row in range(i, rows):
            if matrix[row][j] == '0':
                # we can no longer go down in rows
                return max_area
            else:
                # we can explore further rows
                for col in range(j, right_boundary):
                    # we can keep going right as long as the cell above us is a 1
                    # if we are in first row (i.e. at i) then we don't check the row
                    # above because we don't care about it => not part of our rectangle
                    if matrix[row][col] == '1':
                        # we only continue exploring if the current cell is 1
                        if (row == i) or (matrix[row - 1][col] == '1'):
                            # if we are in first row, the only condition to expand right is if the cell to the right is 1
                            # if we are in other rows, the condition to span right is that the cell to the right has to
                            # be 1 and the one above it has to be 1

                            # we can expand to the right safely
                            current_height = row - i + 1
                            current_width = col - j + 1
                            current_area = current_width * current_height
                            max_area = max(max_area, current_area)
                        else:
                            # we're in row after i and the cell above the current cell is not 1
                            break
                    else:
                        # we update the right_boundary
                        right_boundary = min(right_boundary, col)

                        break

        return max_area

    def maximalRectangle(self, matrix: [[str]]) -> int:
        # we know that matrix is at least 1x1 so below is valid
        rows = len(matrix)
        cols = len(matrix[0])

        max_rectangle_area = 0

        # we need to check the maximum area we can achieve
        # starting at every possible square in matrix
        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j] == '1':
                    cell_max_area = self.getMaxArea(matrix, i, j, rows, cols)
                    max_rectangle_area = max(max_rectangle_area, cell_max_area)

        return max_rectangle_area


'''
    Accepted
    
    Approach 4: Dynamic Programming - Maximum Height at Each Point
    
    The idea here is that we check at each cell[i][j], how far can we go up, go left and go right before we see a 0.
    To avoid recomputing for every cell, we save the results we've seen in the previous row for every col j in 3 arrays:
    height, left and right. The height array is always updated based on current row, if the current cell [i][j] is a 1
    then all we need to do is add 1 to the height we have for cell[i-1][j] => height[j] + 1. If the current cell [i][j] is
    a 0, then we just reset the height counter to be 0 so we can start from scratch in the next row.
    left[j] holds the index of the leftmost 1 such that all the cells between that index and j are 1s. Whenever
    we encounter a 0 cell, we need to set left[j] at 0 so that we don't take it into consideration when we do max when updating
    left[j] in case of cell == 1.
    right[j] holds the index of the rightmost 1 such that all the cells between that index and j are 1s. Unlike the left array,
    the right array is filled from end to start. Whenever we encounter a 0 cell, we need to set right[j] to be cols-1 so that we
    don't take it into consideration when we do min when updating right[j] in case of cell == 1.
'''


class Solution2:
    def maximalRectangle(self, matrix: [[str]]) -> int:
        rows = len(matrix)  # at least 1
        cols = len(matrix[0])  # at least 1

        # we will need 3 arrays to keep track of height, left boundary and right boundary for each column j
        # the arrays height, left and right will have accumulated results as we go from one row to the next
        left = [0] * cols  # initialize all left boundaries to be the leftmost boundary 0
        right = [cols] * cols  # initialize all right boundaries to be the rightmost boundary cols (rightmost column)
        height = [0] * cols  # since we don't know the height at each column, we initialize each to 0

        # this variable will keep track of the maximum area we've seen so far
        max_area = 0

        # now we loop over each row
        for i in range(0, rows):
            # we need to compute the height at every column in current row
            # since height is accumulated from one row to the next, we know that
            # height has the height of each col j from row 0 to i-1. So, if matrix[i][j] == 1
            # it means we need to add 1 to height[j], if we found 0 at matrix[i][j] then the
            # height there is 0 => we reset the height counter
            for j in range(0, cols):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            # now that we're done with updating height of current row, we need to expand the left
            # boundary for each column in current row
            # we start by setting default values for leftmost and rightmost boundaries
            current_left, current_right = 0, cols - 1

            # we start by updating the left boundaries array
            # current_left will always point to the leftmost 1 to the left of j
            # such that there are no 0s between current_left and j
            for j in range(0, cols):
                if matrix[i][j] == '1':
                    # by doing max between 2 indices, we're making sure that we're restricting
                    # the left pointer by the smallest width
                    left[j] = max(left[j], current_left)
                else:
                    # we set the left bound at a '0' to be 0 so that we never choose it when we
                    # do left[j] = max when we have a '1' cell
                    left[j] = 0
                    # the leftmost boundary is now updated to be 1 cell past the current 0 cell
                    current_left = j + 1

            # we now update the right boundaries array
            # current_right will always point to the rightmost 1 to the right of j
            # such that there are no 0s between current_right and j
            for j in range(cols - 1, -1, -1):
                if matrix[i][j] == '1':
                    # by choosing the min between 2 indices, we're restricting the right pointer
                    # by the smallest width
                    # here we chose min instead of max because, unlike the left pointer, here
                    # j is being decremented with every iteration
                    right[j] = min(right[j], current_right)
                else:
                    # we set the right bound at a '0' to be cols so that we never choose it when we
                    # do right[j] = min when we have a '1' cell
                    right[j] = cols - 1
                    current_right = j - 1

            # now we need to compute the areas we have at current row so we can check if one is max
            for j in range(0, cols):
                current_area = (right[j] - left[j] + 1) * height[j]

                max_area = max(max_area, current_area)

        return max_area


'''
    Accepted
    
    Approach 3: Using Histograms + Stack
    
    The idea is to turn the matrix into a set of histograms and then finding the largest rectangle in each histogram and then finding
    the max rectangle among all histograms.
'''


class Solution3:
    def largestRectangleArea(self, heights):
        # we will use this to help us with our algorithm
        # this will contain (index, height) where height is the height of a bar
        # and index is the leftmost index where this particular height can be expanded.
        stack = []

        # this will help us keep track of the max area across the histogram
        max_area = float('-inf')

        for i in range(0, len(heights)):
            left_most_index = -1

            while len(stack) > 0 and stack[len(stack) - 1][1] > heights[i]:
                # while the top of the stack is height that is greater than current height
                # we need to pop that height because it can't expand further
                top_index, top_height = stack.pop()

                # width of top_height is the distance between its starting index and the current index i
                # because it can't expand left past its starting index and it can't expand right past i
                current_area = (i - top_index) * top_height

                max_area = max(max_area, current_area)

                left_most_index = top_index

            # left_most_index marks the left boundary of current height (i.e. the farthest index to which
            # the current height can expand to the left)
            if left_most_index == -1:
                stack.append((i, heights[i]))
            else:
                stack.append((left_most_index, heights[i]))

        # now we need to pop the remaining elements in the stack
        while len(stack) > 0:
            # this bar can expand from top_index all the way to the right
            # so its width is len(heights) - top_index
            top_index, top_height = stack.pop()

            current_area = (len(heights) - top_index) * top_height

            max_area = max(max_area, current_area)

        return max_area

    def maximalRectangle(self, matrix: [[str]]) -> int:
        # we will be incrementally building our set of histograms as we go through each row

        # this will keep track of the max area as we compute
        max_area = 0

        rows = len(matrix)
        cols = len(matrix[0])

        # this will hold our incremental histogram
        heights = [0] * cols

        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j] == '1':
                    heights[j] = heights[j] + 1
                else:
                    heights[j] = 0

            # now that we're done with updating our histogram
            # with an additional row of heights, we need to find the
            # maximum rectangle of this new histogram
            current_max_area = self.largestRectangleArea(heights)

            max_area = max(max_area, current_max_area)

        return max_area


# matrix = [["1", "0", "1", "1", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# matrix = [["0"]]
# matrix = [["1"]]
# matrix = [
#     ["1", "1", "1", "1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1", "1", "1", "0"],
#     ["1", "1", "1", "1", "1", "1", "1", "0"],
#     ["1", "1", "1", "1", "1", "0", "0", "0"],
#     ["0", "1", "1", "1", "1", "0", "0", "0"]
# ]

# matrix = [
#     ["1", "0", "1", "0", "0"],
#     ["1", "0", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "0", "0", "1", "0"]
# ]

print(Solution3().maximalRectangle(matrix))
