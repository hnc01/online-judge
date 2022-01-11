'''
    https://leetcode.com/problems/partition-equal-subset-sum/

    416. Partition Equal Subset Sum

    Given a non-empty array nums containing only positive integers,
    find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
'''


class Solution:
    def can_partition_helper(self, nums, current_num_index, left_subset, right_subset):
        if len(nums) == (len(left_subset) + len(right_subset)):
            # we partitioned all the numbers into 2 subsets
            return sum(left_subset) == sum(right_subset)
        else:
            # we need to check in which subset to place current_num_index
            right_subset_copy = right_subset.copy()
            left_subset_copy = left_subset.copy()

            right_subset_copy.append(nums[current_num_index])
            left_subset_copy.append(nums[current_num_index])

            # we try adding the current number if the right subset and the left subset and see if it works in either one
            return self.can_partition_helper(nums, current_num_index + 1, left_subset, right_subset_copy) \
                   or self.can_partition_helper(nums, current_num_index + 1, left_subset_copy, right_subset)

    def canPartition(self, nums: [int]) -> bool:
        if len(nums) <= 1:
            # an empty array or array one 1 element can't be partitioned into 2 subsets of equal sum
            return False

        return self.can_partition_helper(nums, 0, [], [])


'''
    Same as above but instead of creating the left and right subsets, we just accumulated their sums
'''


class Solution2:
    def can_partition_helper(self, nums, current_num_index, left_subset_sum, right_subset_sum):
        if current_num_index >= len(nums):
            # our current index is no longer inside the nums array so we already placed all elements in the subsets
            return left_subset_sum == right_subset_sum
        else:
            # we need to check in which subset to place current_num_index
            current_num = nums[current_num_index]

            # we try adding the current number if the right subset and the left subset and see if it works in either one
            return self.can_partition_helper(nums, current_num_index + 1, left_subset_sum, right_subset_sum + current_num) \
                   or self.can_partition_helper(nums, current_num_index + 1, left_subset_sum + current_num, right_subset_sum)

    def canPartition(self, nums: [int]) -> bool:
        if len(nums) <= 1:
            # an empty array or array one 1 element can't be partitioned into 2 subsets of equal sum
            return False

        return self.can_partition_helper(nums, 0, 0, 0)


# class Solution3:
#     def can_partition_helper(self, nums, current_num_index, left_subset_sum, right_subset_sum, subset_target_sum):
#         if current_num_index >= len(nums):
#             # our current index is no longer inside the nums array so we already placed all elements in the subsets
#             # check to see if both our subsets reached the goal
#             return left_subset_sum == subset_target_sum and right_subset_sum == subset_target_sum
#         else:
#             # we need to check in which subset to place current_num_index
#             current_num = nums[current_num_index]
#
#             # we try adding the current number if the right subset and the left subset and see if it works in either one
#             can_add_to_left = False
#             can_add_to_right = False
#
#             # we check if we can add the current element to the left subset
#             if current_num + left_subset_sum <= subset_target_sum:
#                 can_add_to_left = self.can_partition_helper(nums, current_num_index + 1, left_subset_sum + current_num, right_subset_sum, subset_target_sum)
#
#             if current_num + right_subset_sum <= subset_target_sum:
#                 can_add_to_right = self.can_partition_helper(nums, current_num_index + 1, left_subset_sum, right_subset_sum + current_num, subset_target_sum)
#
#             return can_add_to_left or can_add_to_right
#
#     def canPartition(self, nums: [int]) -> bool:
#         if len(nums) <= 1:
#             # an empty array or array one 1 element can't be partitioned into 2 subsets of equal sum
#             return False
#
#         # the target sum of each subset is sum(nums) / 2
#         # if the sum is odd then there's no way to reproduce it with 2 subsets because then we'd have floats
#         nums_sum = sum(nums)
#
#         if nums_sum % 2 == 1:
#             # the sum is odd so there's no way to divide it into 2
#             return False
#         else:
#             subset_target_sum = int(nums_sum / 2)
#
#             return self.can_partition_helper(nums, 0, 0, 0, subset_target_sum)

'''
    Accepted but time limit exceeded
'''


class Solution3:
    def can_partition_helper(self, nums, current_num_index, target_sum):
        if target_sum < 0:
            # the current subset we're creating will never sum up to the target sum
            return False
        elif target_sum == 0:
            return True
        else:
            if current_num_index < len(nums):
                # try adding the current element to the subset
                with_current_element = self.can_partition_helper(nums, current_num_index + 1, target_sum - nums[current_num_index])
                without_current_element = self.can_partition_helper(nums, current_num_index + 1, target_sum)

                return with_current_element or without_current_element
            else:
                return False

    def canPartition(self, nums: [int]) -> bool:
        # in this approach we'll utilize the logic in the commented code regarding the target sum
        if len(nums) <= 1:
            # an empty array or array one 1 element can't be partitioned into 2 subsets of equal sum
            return False

        # the target sum of each subset is sum(nums) / 2
        # if the sum is odd then there's no way to reproduce it with 2 subsets because then we'd have floats
        nums_sum = sum(nums)

        if nums_sum % 2 == 1:
            # the sum is odd so there's no way to divide it into 2
            return False
        else:
            subset_target_sum = int(nums_sum / 2)

            # unlike the other approaches, we won't attempt to create both subsets. All we need is one subset
            # to be equal to half of the total sum; automatically, the remaining elements (belonging to the second subset)
            # will sum up to the other half of the total
            return self.can_partition_helper(nums, 0, subset_target_sum)


'''
    DP with memoization (top-down)
'''


class Solution4:
    def can_partition_helper(self, nums, current_num_index, target_sum, memo):
        if target_sum < 0:
            # the current subset we're creating will never sum up to the target sum
            return False

        if target_sum == 0:
            return True

        if target_sum in memo:
            return memo[target_sum]

        if current_num_index < len(nums):
            # try adding the current element to the subset
            with_current_element = self.can_partition_helper(nums, current_num_index + 1, target_sum - nums[current_num_index], memo)
            without_current_element = self.can_partition_helper(nums, current_num_index + 1, target_sum, memo)

            # can we create a subset with current target sum? Yes or No
            memo[target_sum] = with_current_element or without_current_element

            return with_current_element or without_current_element
        else:
            return False

    def canPartition(self, nums: [int]) -> bool:
        # in this approach we'll utilize the logic in the commented code regarding the target sum
        if len(nums) <= 1:
            # an empty array or array one 1 element can't be partitioned into 2 subsets of equal sum
            return False

        # the target sum of each subset is sum(nums) / 2
        # if the sum is odd then there's no way to reproduce it with 2 subsets because then we'd have floats
        nums_sum = sum(nums)

        if nums_sum % 2 == 1:
            # the sum is odd so there's no way to divide it into 2
            return False
        else:
            subset_target_sum = int(nums_sum / 2)

            memo = {}

            # unlike the other approaches, we won't attempt to create both subsets. All we need is one subset
            # to be equal to half of the total sum; automatically, the remaining elements (belonging to the second subset)
            # will sum up to the other half of the total

            # this function call will help us answer: Can we create a subset with target sum subset_target_sum?
            return self.can_partition_helper(nums, 0, subset_target_sum, memo)


class Solution5:
    # in the DP with memoization solution, we have 2 indices changing with every recursive call: current num index and the target sum
    # we'll use these 2 indices to save computed results in our 2-D DP array
    def canPartition(self, nums: [int]) -> bool:
        # we have the same base cases as Solution 4
        # if len(nums) <= 1:
        #     return False

        nums_sum = sum(nums)

        if nums_sum % 2 == 1:
            # the sum is odd so there's no way to divide it into 2
            return False
        else:
            # the first dimension of dp will be index of current number in nums and the second dimension will be the target sum
            # also, just like solutions 4 and 3, we'll focus on building only one of the subsets

            dp = [[]] * len(nums)

            subset_target_sum = int(nums_sum / 2)

            # since it's bottom AND since in the recursive call of Solution4 we're calling target - num, then we need to solve the problems
            # with less target sum until we reach our ultimate target sum
            # ** according to the solution, we need to start the possible target sums with 0 not 1 **
            possible_target_sums = [i for i in range(0, subset_target_sum + 1)]

            # we initiate dp with every possible index in nums and every possible target sum
            for i in range(0, len(nums)):
                dp[i] = [False] * len(possible_target_sums)
                dp[i][0] = True  # we can always produce 2 sets (empty sets) with sum 0 => BASE CASE

            # in each iteration we need to ask the question: should we consider the current element in our subset or no?
            # to answer the question of whether to consider nums[i], we need to see if we have a solution up to i and that adding i will contribute
            # to the solution

            # it's important that the outer loop loops over the elements while the inner loop loops over the target sums
            # in each loop we're basically checking if the current element contributes to the solution that leads to a subset of current target_length
            for i in range(0, len(nums)):
                for target_sum in possible_target_sums:
                    # to guarantee that target_sum - nums[i] doesn't index something negative, we make sure that nums[i] is less than target sum
                    if nums[i] <= target_sum:
                        # with_current_element = self.can_partition_helper(nums, current_num_index + 1, target_sum - nums[current_num_index], memo)
                        # without_current_element = self.can_partition_helper(nums, current_num_index + 1, target_sum, memo)
                        dp[i][target_sum] = dp[i - 1][target_sum] or dp[i - 1][target_sum - nums[i]]  # first clause is WITHOUT nums[i] and second is WITH nums[i]
                    else:
                        # we can't possibly add this element so the solution to dp[i] is the same as dp[i-1]
                        dp[i][target_sum] = dp[i - 1][target_sum]

            return dp[len(nums) - 1][subset_target_sum]


# nums = [1, 5, 11, 5]
# nums = [1, 2, 3, 5]
nums = [14, 9, 8, 4, 3, 2]

# nums = [1, 2, 5]

print(Solution5().canPartition(nums))
