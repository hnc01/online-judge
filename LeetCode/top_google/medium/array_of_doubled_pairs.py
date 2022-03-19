'''
    https://leetcode.com/problems/array-of-doubled-pairs/

    954. Array of Doubled Pairs

    Given an integer array of even length arr, return true if it is possible to reorder arr such that
    arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.
'''

'''
    Accepted
'''

import collections


class Solution:
    def canReorderDoubled(self, arr: [int]) -> bool:
        # this will map each number to its frequency in arr
        occurrences = {}

        for nb in arr:
            if nb not in occurrences:
                occurrences[nb] = 0

            occurrences[nb] += 1

        occurrences = collections.OrderedDict(sorted(occurrences.items()))

        # now we loop over each nb in arr and see if we can find it a double also in arr
        for nb in occurrences:
            # we try to pair off every possible occurrence of the nb
            while occurrences[nb] > 0:
                if (2 * nb) in occurrences and occurrences[(2 * nb)] > 0:
                    # check if the double of the current nb is in occurrences
                    occurrences[2 * nb] -= 1
                    occurrences[nb] -= 1
                elif nb % 2 == 0 and (nb // 2) in occurrences and occurrences[nb // 2] > 0:
                    # check if the half of the current nb is in occurrences (only if nb is pair)
                    occurrences[nb // 2] -= 1
                    occurrences[nb] -= 1
                else:
                    # if there was an occurrence of nb that can't be paired off it means that we will
                    # never find a pair for it so we return False
                    return False

        # we were able to pair off every number in occurrences since we never returned False before this point
        # so we return True here
        return True


print(Solution().canReorderDoubled(arr=[3, 1, 3, 6]))
print(Solution().canReorderDoubled(arr=[2, 1, 2, 6]))
print(Solution().canReorderDoubled(arr=[4, -2, 2, -4]))
print(Solution().canReorderDoubled([2, 4, 0, 0, 8, 1]))
