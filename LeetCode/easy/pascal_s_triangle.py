class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows == 1:
            return [[1]]
        else:
            result = [[1]]
            currentRowNum = 2

            lastRow = [1]

            while currentRowNum <= numRows:
            # generate the new row from lastRow
                currentRow = [1]

                i = 0

                while i + 1 < len(lastRow):
                    currentRow.append(lastRow[i] + lastRow[i+1])
                    i+= 1

                currentRow.append(1)

                lastRow = currentRow
                result.append(lastRow)
                currentRowNum += 1

            return result