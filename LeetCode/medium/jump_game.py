'''
    https://leetcode.com/problems/jump-game/

    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.
'''

'''
    Accepted
'''


class Solution:
    def canJump(self, nums: [int]) -> bool:
        if len(nums) > 1:
            memo = {}

            # we go backwards building our memo to see if we can reach the last index from each step
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] >= (len(nums) - 1 - i):
                    memo[i] = True
                else:
                    # check if it can be reached by any number of jumps
                    # we've already checked all the possible jumps after i and stored
                    # their results in memo so we need to check only memo to see if we can reach
                    # the last index from here
                    can_reach = False

                    # since we can reach the end more quickly with bigger jumps, we will examine the jumps
                    # we can make from highest to lowest
                    # second thing, we don't care about jumps that are beyond our nums' length so we statured first_jump
                    # to the max jump that can actually reach nums's end and not surpass it
                    first_jump = nums[i]

                    if i + first_jump >= len(nums):
                        first_jump = len(nums) - 1 - i

                    # we need to start with highest first possible jump and end at 1
                    for j in range(first_jump, 0, -1):
                        index_to_check = i + j

                        if memo[index_to_check]:
                            can_reach = True
                            break

                    memo[i] = can_reach

            return memo[0]
        else:
            return True


print(Solution().canJump([3, 2, 1, 0, 4]))
