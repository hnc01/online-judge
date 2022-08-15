class Solution:
    def canBeIncreasing(self, nums: [int]) -> bool:
        def isStrictlyIncreasing(arr):
            for i in range(0, len(arr) - 1):
                if arr[i] >= arr[i+1]:
                    return False
            return True

        if isStrictlyIncreasing(nums):
            return True

        for i in range(0, len(nums)):
            # consider removing nums[i]
            if isStrictlyIncreasing(nums[0:i] + nums[i+1:len(nums)]):
                return True

        return False
