'''
    https://leetcode.com/problems/target-sum/

    494. Target Sum

    You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
    and then concatenate all the integers.

        - For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

    Return the number of different expressions that you can build, which evaluates to target.
'''


class Solution:
    def find_target_sum_ways_helper(self, nums, index, sum_so_far, target):
        if index >= len(nums):
            # we went through all the numbers and assigned a sign to each one
            # now we just need to see if the current path lead to an expression that evaluates to target
            if sum_so_far == target:
                # adding 1 to the total sum of valid expressions
                return 1
            else:
                # adding 0 to the total sum of valid expressions
                return 0
        else:
            current_num = nums[index]

            # we need to go down the paths of +current_num and -current_num to see if one or both lead to the target sum
            return self.find_target_sum_ways_helper(nums, index + 1, sum_so_far + current_num, target) \
                   + self.find_target_sum_ways_helper(nums, index + 1, sum_so_far - current_num, target)

    def findTargetSumWays(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            # if we don't have any numbers then we can't build any expressions
            return 0

        return self.find_target_sum_ways_helper(nums, 0, 0, target)


'''
    Let's try to do the same solution but without making use of sum_so_far
'''


class Solution2:
    def find_target_sum_ways_helper(self, nums, index, target):
        if index >= len(nums):
            # we went through all the numbers and assigned a sign to each one
            # now we just need to see if the current path lead to an expression that evaluates to target
            if target == 0:
                # adding 1 to the total sum of valid expressions
                return 1
            else:
                # adding 0 to the total sum of valid expressions
                return 0
        else:
            current_num = nums[index]

            # we need to go down the paths of +current_num and -current_num to see if one or both lead to the target sum
            return self.find_target_sum_ways_helper(nums, index + 1, target + current_num) \
                   + self.find_target_sum_ways_helper(nums, index + 1, target - current_num)

    def findTargetSumWays(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            # if we don't have any numbers then we can't build any expressions
            return 0

        return self.find_target_sum_ways_helper(nums, 0, target)


'''
    Let's try with memoization
'''

'''
    Accepted
    
    The reason why we used a 2-D array is because both the index of the current element and the target are changing with every
    recursive function call.
'''


class Solution3:
    def find_target_sum_ways_helper(self, nums, index, target, memo):
        if index >= len(nums):
            # we went through all the numbers and assigned a sign to each one
            # now we just need to see if the current path lead to an expression that evaluates to target
            if target == 0:
                # adding 1 to the total sum of valid expressions
                return 1
            else:
                # adding 0 to the total sum of valid expressions
                return 0
        elif target in memo[index]:
            return memo[index][target]
        else:
            current_num = nums[index]

            # we need to go down the paths of +current_num and -current_num to see if one or both lead to the target sum
            current_num_results = self.find_target_sum_ways_helper(nums, index + 1, target + current_num, memo) \
                                  + self.find_target_sum_ways_helper(nums, index + 1, target - current_num, memo)

            memo[index][target] = current_num_results

            return current_num_results

    def findTargetSumWays(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            # if we don't have any numbers then we can't build any expressions
            return 0

        memo = [{}] * len(nums)

        for i in range(0, len(nums)):
            memo[i] = {}

        return self.find_target_sum_ways_helper(nums, 0, target, memo)


'''
    This is needed to understand the equations in the below loop

    # this recursive call: self.find_target_sum_ways_helper(nums, index + 1, target + current_num)) \
        #        + self.find_target_sum_ways_helper(nums, index + 1, target  + (- current_num))
        # gives us:
        # dp[i][current_target] = dp[i + 1][current_target + current_num] + dp[i + 1][current_target - current_num]
        #
        # from this we can get 2 equations:
        # dp[i + 1][current_target - current_num] = dp[i][current_target] - dp[i + 1][current_target + current_num]
        # dp[i + 1][current_target + current_num] = dp[i][current_target] - dp[i + 1][current_target - current_num]

        # now we can do -1 to the index dimension to get rid of the i + 1 (the i + 1 would force us to fill the dp array
        # from greatest index to smallest index).
        # dp[i][current_target - current_num] = dp[i-1][current_target] - dp[i][current_target + current_num]
        # dp[i][current_target + current_num] = dp[i-1][current_target] - dp[i][current_target - current_num]
        #
        # We know that - dp[i][current_target + current_num] = dp[i][current_target - current_num] (we can refer to the tree of expressions
        # to see this symmetry). Similarly, - dp[i][current_target - current_num] = dp[i][current_target + current_num]. We replace:
        #
        # dp[i][current_target - current_num] = dp[i-1][current_target] + dp[i][current_target - current_num]
        # dp[i][current_target + current_num] = dp[i-1][current_target] + dp[i][current_target + current_num]

        # since we call i-1 in the loop, we can't start with i=0
        
'''
'''
    DP bottom up: Accepted
'''


class Solution4:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        # this is the max sum we can get out of our numbers
        total = sum(nums)

        if int(abs(target)) > total:
            # the numbers we can't possibly generate target so we return 0
            return 0

        dp = [[]] * len(nums)

        # the length of the second dimensions is 2 x the max total. Why? because we want to include
        # in this second dimension all indexes from -total to total so that's double total. But how will we index
        # the negative parts of the total? i.e., from -total to 0. We do this by adding an offset to all our indexes
        # so when we index something from -total to 0 and we add total to it, it automatically offsets to a sum >= 0.
        # As a consequence, when we index something from 0 to total, the resulting index will fall in the range from total to 2 * total.
        for i in range(0, len(nums)):
            dp[i] = [0] * (2 * total + 1)

        # base cases:
        dp[0][nums[0] + total] = 1  # if our substring is only the first number and our target equals the first number, then we reached our target so 1
        dp[0][-nums[0] + total] += 1  # we do += 1 because if nums[0] is 0 then we need to account twice for this so we need +=1 to be 2. Otherwise, +=1 would just equal 1.

        for i in range(1, len(nums)):
            # instead of looping over all possible targets like we did in my solution, here we loop over all possible sums
            # that can be generated by nums
            for current_sum in range(-total, total + 1):
                if (current_sum + nums[i] + total) < (2 * total + 1):
                    dp[i][current_sum + nums[i] + total] += dp[i - 1][current_sum + total]

                if (current_sum - nums[i] + total) < (2 * total + 1):
                    dp[i][current_sum - nums[i] + total] += dp[i - 1][current_sum + total]

        # since we're offsetting the indexes of the second dimension by 'total', when we're returning the solution, we also need to offset by total
        return dp[len(nums) - 1][target + total]


# nums = [1, 1, 1, 1, 1]
# target = 3

# nums = [1]
# target = 1

# nums = [1000]
# target = -1000

# nums = [1, 2, 1]
# target = 0

nums = [11, 19, 14, 50, 47, 35, 18, 32, 8, 2, 31, 45, 6, 25, 49, 23, 25, 33, 24, 33]
target = 44

print(Solution5().findTargetSumWays(nums, target))
