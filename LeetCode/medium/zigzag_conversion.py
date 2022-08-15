class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # we need to map every character in s to its row in the zigzag pattern

        # it will map every row to  its string
        rowsMap = {}

        for r in range(0, numRows):
            rowsMap[r] = ""

        # i will be the index going through s and
        i = 0

        while i < len(s):
            # r will be the row index
            r = 0

            while i < len(s) and r < numRows:
                rowsMap[r] += s[i]
                r += 1
                i += 1

            # decrement to go 1 step before the last row
            r -= 2

            # now r is == len(s) we need to do r - 1 and keep decrementing until it’s 1
            while i < len(s) and r > 0:
                rowsMap[r] += s[i]
                r -= 1
                i += 1

        # now we need to go through the rows array and combine characters in the same row together
        result = ""

        for r in range(0, numRows):
            result += rowsMap[r]

        return result