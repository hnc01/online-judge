'''
    https://leetcode.com/problems/longest-increasing-subsequence/

    300. Longest Increasing Subsequence

    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    A subsequence is a sequence that can be derived from an array by deleting some or no elements without
    changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''


class Solution:
    def length_of_lis_helper(self, nums, prev, cur):
        if cur >= len(nums):
            # when we surpass the length of the string, we can't form any additional subsequences
            return 0

        # we either take current element or we don't
        # if we take it, it has to be more than nums[prev]
        length_with_cur = 0

        # it means we have accumulated a sequence so far (not at the start)
        # to take the current element, it has to be > nums[prev]
        if prev >= 0:
            if nums[cur] > nums[prev]:
                # we can have the option of taking the current element
                length_with_cur = 1 + self.length_of_lis_helper(nums, cur, cur + 1)
        else:
            # we can't compare cur with previous element so we just consider it
            length_with_cur = 1 + self.length_of_lis_helper(nums, cur, cur + 1)

        # either way we can skip the current element so prev remains the same
        length_without_cur = self.length_of_lis_helper(nums, prev, cur + 1)

        # for current element we return the max of both lengths
        return int(max(length_with_cur, length_without_cur))

    def lengthOfLIS(self, nums: [int]) -> int:
        return self.length_of_lis_helper(nums, -1, 0)


'''
    Accepted DP-Solution
    
    Idea is that we start from index 0 and we keep going until the end of the array. Each time, we examine the longest subsequence ending at i.
    The longest subsequence ending at i is always [the longest subsequence ending at any of the elements that are before i such that nums[j] < nums[i]] + 1
    We need to examine only the elements before the current element if they are less than it; adding the current element won't lead to an
    increasing subsequence.  
'''


class Solution2:
    def lengthOfLIS(self, nums: [int]) -> int:
        cache = {}

        overall_max_subsequence_length = 0

        for i in range(0, len(nums)):
            ending_with = nums[i]

            max_subsequence_length = 0

            for j in range(0, i):
                if nums[j] < ending_with:
                    max_subsequence_length = int(max(max_subsequence_length, cache[j]))

            # to account for adding the current element to the longest subsequence of all the elements less than it from 0 to i
            max_subsequence_length += 1

            cache[i] = max_subsequence_length

            overall_max_subsequence_length = int(max(overall_max_subsequence_length, cache[i]))

        return overall_max_subsequence_length


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# nums = [0,1,0,3,2,3]
# nums = [7, 7, 7, 7, 7, 7, 7]
nums = [4, 3, 2, 1]

print(Solution2().lengthOfLIS(nums))
