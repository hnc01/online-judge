'''
    https://leetcode.com/problems/minimum-size-subarray-sum/

    209. Minimum Size Subarray Sum

    Given an array of positive integers nums and a positive integer target, return the minimal length of a
    contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
    If there is no such subarray, return 0 instead.
'''

import math

'''
    Accepted
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        # we will try the sliding window method and we'll have 2 indices l and r
        # we will keep l in its place and keep incrementing r until we have sum >= target
        # we will note the length of subarray, now while the sum of the subarray >= target
        # we keep doing l += 1. When the loop breaks, we note the length of the subarray
        # and move on by doing r += 1
        l, r = 0, 0
        subArraySum = 0
        minLength = float('inf')

        while l < len(nums) and r < len(nums):
            subArraySum += nums[r]

            while l < len(nums) and subArraySum >= target:
                minLength = min(minLength, r - l + 1)
                subArraySum -= nums[l]
                l += 1

            # we reach here because either l >= len(sums)
            # or the subArraySum < target => need to do r + 1
            r += 1

        if math.isinf(minLength):
            return 0

        return minLength
