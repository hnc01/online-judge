'''
    https://leetcode.com/problems/search-in-rotated-sorted-array/

    There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting
    array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated
    at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    You must write an algorithm with O(log n) runtime complexity.
'''

'''
    Accepted
'''

class Solution:
    def search_helper(self, nums, start, end, target):
        if (end - start) + 1 == 1:
            # we have one element left in the list
            if nums[start] == target:
                return start
            else:
                return -1
        else:
            pivot = int((start + end) / 2)

            if nums[pivot] == target:
                return pivot
            else:
                # need to check if the pivot is inside the first ascending list or the second ascending list
                if nums[pivot] >= nums[start]:
                    # we are in first ascending list
                    if target >= nums[start] and target < nums[pivot]: # TODO fix this condition
                        # go left
                        return self.search_helper(nums, start, pivot-1, target)
                    else:
                        # go right
                        return self.search_helper(nums, pivot+1, end, target)
                else:
                    # we are in second ascending list
                    if target <= nums[end] and target > nums[pivot]:
                        # go right
                        return self.search_helper(nums, pivot + 1, end, target)
                    else:
                        # go left
                        return self.search_helper(nums, start, pivot - 1, target)

    def search(self, nums: [int], target: int) -> int:
        return self.search_helper(nums, 0, len(nums) - 1, target)

print(Solution().search([1], 0))
