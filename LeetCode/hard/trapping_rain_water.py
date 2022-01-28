'''
    https://leetcode.com/problems/trapping-rain-water/

    42. Trapping Rain Water

    Given n non-negative integers representing an elevation map
    where the width of each bar is 1, compute how much water it can trap after raining.
'''

'''
    Time Limit Exceeded. Because we are looping over levels which is way more than O(n).
'''


class Solution:
    def trap(self, height: [int]) -> int:
        # this will accumulate all the gaps we have that could be filled with water
        total_gap = 0

        # we will start level by level and for patterns where we have
        # height -> 0 -> height => these are our gaps
        # first we need to remove from height all trailing zeros left and right
        start_index = 0
        end_index = len(height) - 1

        while True:
            while start_index < len(height) and height[start_index] == 0:
                start_index += 1

            while end_index >= 0 and height[end_index] == 0:
                end_index -= 1

            if start_index < end_index:
                # we have a valid graph left => it's not all flat and it doesn't
                # start or end with 0s
                # now we will examine the heights array only from start_index to end_index

                # we will keep go through the heights array and look for the pattern:
                # height -> 0 .. 0 -> height
                # we know already that start_index is not 0
                i = start_index
                j = start_index + 1

                while i <= end_index and j <= end_index:
                    # we need j to find the first 0 after i
                    # if there are no 0s between i and j then
                    # they both need to keep moving to the right until we find the first height -> 0 pattern
                    while i <= end_index and j <= end_index and height[j] != 0:
                        i += 1
                        j += 1

                    if i <= end_index and j <= end_index:
                        # if it was able to find then we need to keep looping until we find
                        # the first height bigger than 0
                        while j <= end_index and height[j] == 0:
                            j += 1

                        # we reach this point if: j > end_index (i.e. couldn't find 0s) or height[j] != 0 (need to compute gap)
                        if j > end_index:
                            # we couldn't find any 0s at this level so we need break to move on to next level
                            break
                        else:
                            # we found our first height -> 0 ... 0 -> height
                            # we need to compute its gap
                            total_gap += j - i - 1

                            # now our new starting point is j
                            i = j
                            j += 1
                    else:
                        # we couldn't find any 0s at this level so we need break to move on to next level
                        break

                # when we reach this point, it means we finished an entire level, so we need to remove it
                for h in range(start_index, end_index + 1):
                    if height[h] > 0:
                        height[h] -= 1
            else:
                break

        return total_gap


'''
    The only solution is to loop over the height array only and compute.
    
    Accepted
'''


class Solution2:
    def trap(self, height: [int]) -> int:
        # to keep track of total gap
        gap = 0

        # we will use start and end to discard trailing 0s at
        # the beginning and end of height
        start = 0
        end = len(height) - 1

        while start < len(height) and height[start] == 0:
            start += 1

        while end >= 0 and height[end] == 0:
            end -= 1

        # now we have start at the first height that's non-zero
        # now we have end at the last height that's non-zero
        if start < end:
            # it means that we have at least 1 height that's not 0

            # we'll use left to keep track of our left-most height
            left = start

            while left <= end:
                # we'll use right to keep track of our right-most height
                right = left + 1

                # needed to compute space that could be occupied by water
                heights_in_between = 0

                # we need to find the tallest height taller than left
                while right <= end and height[right] < height[left]:
                    heights_in_between += height[right]

                    right += 1

                # when we exit the above loop, we either have right > end
                # or height[right] >= height[left]
                if right <= end:
                    # computing the area between the left and right heights
                    # and removing the heights in between to get the exact
                    # amount of space the water can occupy
                    gap += (min(height[left], height[right]) * (right - left - 1)) - heights_in_between
                    # we move our left pointer to this right tower
                    left = right
                else:
                    # we couldn't find a height taller than left
                    # so we need to find the tallest height among all heights after left
                    right = left + 1

                    max_height = 0
                    max_height_index = -1

                    # needed to compute space that could be occupied by water
                    heights_in_between = 0
                    temp_heights_in_between = 0

                    while right <= end:
                        if height[right] <= max_height:
                            temp_heights_in_between += height[right]
                        else:
                            # the height we found is more than max
                            # everything we accumulated in temp_heights should be added to heights
                            max_height = height[right]
                            max_height_index = right
                            heights_in_between += temp_heights_in_between
                            # we set it height at right because we might find a higher level after this
                            # and at that point we'll need height[right] to be included in temp_heights
                            temp_heights_in_between = height[right]

                        right += 1

                    if max_height_index >= 0:
                        # we found a max height after left
                        right = max_height_index

                        if right <= end:
                            # now we compute the area between left and the first non-zero height we found
                            if (right - left) >= 2:
                                # there is at least one empty space between them
                                gap += (height[right] * (right - left - 1)) - heights_in_between

                            # we move our left pointer to this right tower
                            left = right
                        else:
                            # we couldn't find a non-zero tower
                            break
                    else:
                        # we couldn't find a max height after left so they're all 0s
                        break

            return gap
        else:
            # the entire heights array is made up of 0s so we the solution is 0
            return 0


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]
# height = [4, 2, 3]
# height = [4, 3, 2]
# height = [5,4,1,2]

print(Solution2().trap(height))
