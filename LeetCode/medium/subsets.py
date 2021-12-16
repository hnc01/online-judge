'''
    https://leetcode.com/problems/subsets/

    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
'''

'''
    Accepted
'''


class Solution:
    # at each step we need to consider the case where we take the current element or we don't take it
    def subsets_helper(self, nums, i, current_subset, solution):
        if i >= len(nums):
            # we already explored all our elements
            solution.append(current_subset)
        else:
            # we either take the element at i or we don't
            current_subset_without = current_subset.copy()
            current_subset_with = current_subset.copy()
            current_subset_with.append(nums[i])

            self.subsets_helper(nums, i + 1, current_subset_without, solution)
            self.subsets_helper(nums, i + 1, current_subset_with, solution)

    def subsets(self, nums: [int]) -> [[int]]:
        solution = []

        self.subsets_helper(nums, 0, [], solution)

        return solution


print(Solution().subsets([1, 2, 3]))
