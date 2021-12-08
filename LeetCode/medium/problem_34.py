'''
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
'''

'''
    Accepted
'''

class Solution:
    def search_range_helper(self, nums, start, end, target):
        if end <= start:
            # we have one element
            if nums[start] == target:
                return [start, end]
            else:
                return [-1, -1]
        else:
            pivot = int((start + end) / 2)

            if nums[pivot] == target:
                start_index = pivot
                end_index = pivot

                while start_index >= start and nums[start_index] == target:
                    start_index -= 1

                while end_index <= end and nums[end_index] == target:
                    end_index += 1

                return [start_index + 1, end_index - 1]
            else:
                if target > nums[pivot]:
                    # go right
                    return self.search_range_helper(nums, pivot + 1, end, target)
                else:
                    # go left
                    return self.search_range_helper(nums, start, pivot - 1, target)

    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums) == 0:
            return [-1, -1]
        else:
            return self.search_range_helper(nums, 0, len(nums) - 1, target)

print(Solution().searchRange([2,2], 1))
