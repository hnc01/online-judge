class Solution:
    def findMissingRanges(self, nums: [int], lower: int, upper: int) -> [str]:
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]

        missingRanges = []

        # missing ranges start before nums[0]
        # missing ranges in the middle of nums
        # missing ranges after nums[-1]
        if nums[0] > lower:
            # our first missing range is from lower to nums[0] - 1
            if lower == nums[0] - 1:
                missingRanges.append(str(lower))
            else:
                missingRanges.append(str(lower) + "->" + str(nums[0] - 1))

        for i in range(0, len(nums)):
            if i + 1 < len(nums) and nums[i + 1] - nums[i] > 1:
                # there’s a missing range between nums[i] and nums[i+1]
                # that range is nums[i] + 1 -> nums[i+1] - 1
                if nums[i] + 1 == nums[i + 1] - 1:
                    missingRanges.append(str(nums[i] + 1))
                else:
                    missingRanges.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))

        if nums[-1] < upper:
            if upper == nums[-1] + 1:
                missingRanges.append(str(upper))
            else:
                missingRanges.append(str(nums[-1] + 1) + "->" + str(upper))

        return missingRanges