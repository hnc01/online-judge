'''
    https://leetcode.com/problems/find-original-array-from-doubled-array/

    2007. Find Original Array From Doubled Array

    An integer array original is transformed into a doubled array changed by appending twice the
    value of every element in original, and then randomly shuffling the resulting array.

    Given an array changed, return original if changed is a doubled array. If changed is not a doubled array,
    return an empty array. The elements in original may be returned in any order.
'''

'''
    Accepted
'''


class Solution:
    def findOriginalArray(self, changed: [int]) -> [int]:
        if len(changed) <= 1:
            return []

        # will hold the original array to return
        original = []

        # maps every element to its count (so that we're sure every element is used only once)
        counts = {}

        for num in changed:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # we sort the unique numbers so we can make sure our pairings don't eliminate other valid pairings
        # by always looking for the double of the smallest numbers (avoid looking for the halves)
        sorted_nums = sorted(counts.keys())

        for i in range(0, len(sorted_nums)):
            current_num = sorted_nums[i]

            while counts[current_num] > 0:
                # we need to keep pairing off the current number and until we're done with it
                # we haven't already paired off this number
                # the only special case we need to take care of is 0 because 0 * 2 == 0 // 2 = 0
                if current_num == 0:
                    if counts[current_num] >= 2:
                        # we can pair off 2 of the 0s
                        counts[current_num] -= 2

                        original.append(current_num)
                    else:
                        # we found a 0 that we can't pair off, it means there's no solution
                        return []
                else:
                    # since we sorted our numbers in ascending order, we should always only look
                    # for the doubles and not the half because the half is less than the current num
                    # and all the numbers less than current num have already been paired off
                    if (current_num * 2) in counts and counts[current_num * 2] > 0:
                        # we found its double
                        counts[current_num] -= 1
                        counts[current_num * 2] -= 1

                        original.append(current_num)
                    else:
                        # we couldn't find a half or double for it, it means there's no solution
                        return []

        # if we reached this point and never returned [] then we found a solution
        return original


print(Solution().findOriginalArray([1, 3, 4, 2, 6, 8]))
print(Solution().findOriginalArray([6, 3, 0, 1]))
print(Solution().findOriginalArray([6, 3, 0, 1, 0, 2]))
print(Solution().findOriginalArray([1]))
print(Solution().findOriginalArray([]))
print(Solution().findOriginalArray([3, 1]))
print(Solution().findOriginalArray([4, 4, 16, 20, 8, 8, 2, 10]))
