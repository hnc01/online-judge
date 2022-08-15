class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        def helper(nums, i, sum, target, dp):
            if sum == target:
                return 1
            elif sum > target:
                return 0
            elif(i, sum) in dp:
                return dp[(i, sum)]
            else:
                count = 0

                # either consider nums[j] as part of my sum
                for j in range(0, len(nums)):
                    count += helper(nums, j, sum + nums[j], target, dp)

                dp[(i, sum)] = count

                return count

        count = 0
        dp = {}

        for i in range(0, len(nums)):
            # this function call with answer: how many combinations of sum start with nums[i]
            count += helper(nums, i, nums[i], target, dp)

        return count
