'''
    https://leetcode.com/problems/house-robber/

    198. House Robber

    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them
    is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses
    were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight
    without alerting the police.
'''

'''
    Accepted but time limit exceeded
'''


class Solution:
    def rob_helper(self, nums, current_house):
        if current_house >= len(nums):
            # we have checked all our options for current combination
            return 0
        else:
            # we either rob the current house or not
            # if we rob current house we can't consider the house right after it

            # consider the current house: nums after removing current_house and current_house + 1 and adding current_house total_money
            # not consider the current house: nums removing current_house but not adding it to total_money

            return max(nums[current_house] + self.rob_helper(nums, current_house + 2), self.rob_helper(nums, current_house + 1))

    def rob(self, nums: [int]) -> int:
        return self.rob_helper(nums, 0)


'''
    DP using memoization (top-down)
'''


class Solution2:
    def rob_helper(self, nums, current_house, memo):
        if current_house >= len(nums):
            # we have checked all our options for current combination
            return 0
        elif current_house in memo:
            return memo[current_house]
        else:
            # we either rob the current house or not
            # if we rob current house we can't consider the house right after it

            # consider the current house: nums after removing current_house and current_house + 1 and adding current_house total_money
            # not consider the current house: nums removing current_house but not adding it to total_money
            current_house_max = max(nums[current_house] + self.rob_helper(nums, current_house + 2, memo), self.rob_helper(nums, current_house + 1, memo))

            memo[current_house] = current_house_max

            return current_house_max

    def rob(self, nums: [int]) -> int:
        memo = {}

        return self.rob_helper(nums, 0, memo)


'''
    Accepted: DP (bottom up)
'''


class Solution3:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0

        # the indices we are referring to in the memoization problem are always current_house + 1 and current_house + 2
        # so, these 2 indices should be the queries to our DP table
        max_profit = [0] * (len(nums) + 1)  # max_profit[i] is the maximum profit we can achieve by robbing houses from i onwards

        # we need to initialize some values in the array before we start
        # we check the base case of our recursive algorithm
        # in our case case, when we exceed the length of the array, we return 0
        # this means that we need to expand our max_profit array by 1 slot to cater for the `exceed length` step
        # this is why max_profit is initialized with length len(nums) + 1 and not just len(nums)
        max_profit[len(nums)] = 0  # case when we exceed length
        max_profit[len(nums) - 1] = nums[len(nums) - 1]  # if we rob only the last house

        # since the indices we will be using are +1 and +2, it means that we need to solve the problem from end to start
        # because to solve problem at i we need i+1 and i+2 to be solved
        # start from the end and go back 1 step at a time
        for i in range(len(nums) - 2, -1, -1):
            # in the recursive approach, we add the profit of the current house when we skip the next house => case of i + 2
            max_profit[i] = max(max_profit[i + 1], max_profit[i + 2] + nums[i])

        return max_profit[0]


nums = [1, 2, 1, 1]

print(Solution3().rob(nums))
