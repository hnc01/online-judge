'''
    https://leetcode.com/problems/search-a-2d-matrix-ii/

    240. Search a 2D Matrix II

    Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
        - Integers in each row are sorted in ascending from left to right.
        - Integers in each column are sorted in ascending from top to bottom.
'''

'''
    Accepted
'''


class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for col in range(0, n):
            if matrix[0][col] == target:
                return True
            elif matrix[0][col] > target:
                # there's no way we can find it moving forward
                break
            else:
                # if matrix[0][col] < target:
                # we need to search the column IF the cell at [row][col] < target
                # there's a chance to find it in the column
                for row in range(1, m):
                    if matrix[row][col] == target:
                        return True
                    elif matrix[row][col] > target:
                        # we reached a point in the column where the numbers are larger than target
                        break

        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 30

print(Solution().searchMatrix(matrix, target))
