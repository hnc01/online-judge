'''
    https://leetcode.com/problems/jump-game-ii/

    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Your goal is to reach the last index in the minimum number of jumps.

    You can assume that you can always reach the last index.
'''

'''
    Accepted
'''


class Solution:
    def jump_helper(self, nums, position, memo):
        if position in memo:
            return memo[position]
        elif position == len(nums) - 1:
            # we reached the end so we shouldn't just anymore
            return 0
        elif position >= len(nums):
            # we surpassed the end so the current path isn't good
            return float("inf")
        else:
            # we are still able to make jumps
            max_jumps = nums[position]

            minimum_jumps_from_position = float("inf")

            for nb_of_jumps in range(1, max_jumps + 1):
                jumps = 1 + self.jump_helper(nums, position + nb_of_jumps, memo)

                if jumps < minimum_jumps_from_position:
                    minimum_jumps_from_position = jumps

            memo[position] = minimum_jumps_from_position

            return minimum_jumps_from_position

    def jump(self, nums: [int]) -> int:
        memo = {}

        return self.jump_helper(nums, 0, memo)


'''
    Suggested Solution by LeetCode using Greedy Approach: always pick the jump that will take you furthest on the next jump
'''


class Solution2:
    def jump(self, nums: [int]) -> int:
        jumps = 0 # we only increase it when we're done examining all positions from previous to current_jump_end and then we expand
        # the jump window to the farthest possible
        current_jump_end = 0 # the farthest position we can reach from previous position we examined
        farthest = 0 # farthest we can reach out of all positions from previous to current_jump_end

        for i in range(len(nums) - 1):
            # we continuously find the how far we can reach in the current jump
            farthest = max(farthest, i + nums[i])
            # if we have come to the end of the current jump,
            # we need to make another jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest

        return jumps


print(Solution2().jump([2,3,1,1,4]))
