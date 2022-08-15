class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if rowIndex == 0:
            return [1]
        else:
            currentRowIndex = 1

            lastRow = [1]

            while currentRowIndex <= rowIndex:
                # generate the new row from lastRow
                currentRow = [1]

                i = 0

                while i + 1 < len(lastRow):
                    currentRow.append(lastRow[i] + lastRow[i+1])
                    i+= 1

                currentRow.append(1)

                lastRow = currentRow
                currentRowIndex += 1

            return lastRow
