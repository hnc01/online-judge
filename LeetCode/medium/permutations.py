'''
    https://leetcode.com/problems/permutations/

    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

'''
    Accepted
'''

class Solution:
    def permute_helper(self, nums, current_result, results):
        if len(nums) == len(current_result):
            # we added all the numbers in nums so we can add the current result to the list
            results.append(current_result)
        else:
            for i in range(0, len(nums)):
                if nums[i] not in current_result:
                    current_result_copy = current_result.copy()
                    current_result_copy.append(nums[i])

                    self.permute_helper(nums, current_result_copy, results)

    def permute(self, nums: [int]) -> [[int]]:
        results = []

        for i in range(0, len(nums)):
            # get all the permutations starting with digit at nums[i]
            self.permute_helper(nums, [nums[i]], results)

        return results

print(Solution().permute([1,0]))