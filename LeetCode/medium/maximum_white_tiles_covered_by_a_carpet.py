class Solution:
    def maximumWhiteTiles(self, tiles: [[int]], carpetLen: int) -> int:
        '''
            1- sort the tiles by li in ascending order

            2- Try placing the carpet at every starting position of a range of tiles. For example, if we have [1,5], [10, 11],
            [12, 18], we first try to placet the carpet at position 1, then 10 and then 12. Why? Because starting the carpet at any other
            position will lead to the carpet covering tiles that are not white and we don't care about such placements.

            3- After placing the carpet[0] at a known position (starting range of tiles), we need to check where our carpet[1] will land. This can be done by simply adding carpetLen to carpet[0]. Now, we have to find the number of white tiles between carpet[0] and carpet[1].
            We have 3 different cases: (a) carpet[1] will land inside the same tile range of carpet[0], (b) will lie in a non-white range after the carpet[0] tile range (c) will lie in a white range after the range of carpet[0].

            we can use prefix sum to get the total number of white tiles between the white ranges.
            tiles[0] = [1, 5]
            tiles[1] = [10, 11]
            tiles[2] = [12, 18]

            preSum[0] = number of white between ranges 0 and 0 is (5-1) + 1 = 5 white tiles
            preSum[1] = number of white between ranges 0 and 1 is 5 + (11 - 10) + 1 = 5 + 2 = 7
            preSum[2] = number of white between ranges 0 and 2 is 7 + (18 - 12) + 1 = 7 + 7 = 14

            To get the number of white tiles between 1 and 2, we just need to remove preSum[0] from preSum[2].

            So now, given ranges, we can quickly find the number of white tiles between them.

            4- The last problem to figure out is how to quickly find the end range where carpet[1] lands (without examining all ranges). We use binary search: if the index is inside a range, we return range. Otherwise, if index < range[0], we search before. Else, we search after.
        '''

        # sorting in ascending order by li
        tiles = sorted(tiles, key=lambda x: x[0])

        def findTilesRange(end, low, high):
            if low > high:
                # we couldn't find end in any range
                return high
            else:
                # get the mid range
                mid = low + ((high - low) // 2)

                if tiles[mid][0] <= end <= tiles[mid][1]:
                    return mid
                elif end < tiles[mid][0]:
                    return findTilesRange(end, low, mid - 1)
                elif end > tiles[mid][1]:
                    return findTilesRange(end, mid + 1, high)

        # then we calculate preSum which would tell us the number of white tiles between ranges
        # pre[i] = number of white tiles between range[0] and range[i]
        # start with preSum[0] = number of white tiles of range tiles[0]
        preSum = {}
        preSum[-1] = 0
        preSum[0] = (tiles[0][1] - tiles[0][0]) + 1

        for i in range(1, len(tiles)):
            currentRangeTilesCount = (tiles[i][1] - tiles[i][0]) + 1
            preSum[i] = preSum[i - 1] + currentRangeTilesCount

        maximumTilesCovered = 0

        # now we try to place the carpet at the beginning of every range
        for i in range(0, len(tiles)):
            carpetStart = tiles[i][0]
            carpetEnd = carpetStart + carpetLen - 1

            # now we need to find carpetEnd belongs to which range. If it doesn't belong to any white range, we need
            # the binary search function to return the index of the largest range right before carpetEnd
            rangeStart = i
            rangeEnd = findTilesRange(carpetEnd, 0, len(tiles) - 1)

            # now we need to get the number of white tiles between rangeStart and rangeEnd
            # we know that rangeStart is covered from the start but rangeEnd may be covered in part.
            if carpetEnd >= tiles[rangeEnd][1]:
                # rangeEnd is covered in entirety
                numberOfWhiteTiles = preSum[rangeEnd] - preSum[rangeStart - 1]
            else:
                # carpetEnd is somewhere in the range so we need to remove the remaining tiles on the right
                numberOfWhiteTiles = preSum[rangeEnd] - preSum[rangeStart - 1]

                # we need to remove more tiles that are to the right of carpetEnd in rangeEnd tiles
                numberOfWhiteTiles -= tiles[rangeEnd][1] - carpetEnd

            maximumTilesCovered = max(maximumTilesCovered, numberOfWhiteTiles)

        return maximumTilesCovered