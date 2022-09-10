class Solution:
    def majorityElement(self, nums: list) -> int:
        candidate = nums[0]

        # we've already seen candidate so we have votes = 1 and we start
        # our process with i = 1
        votes = 1

        for i in range(1, len(nums)):
            if votes == 0:
                # we update our candidate because we already paired off
                # as much of the current candidate as we have other elements
                candidate = nums[i]

            if nums[i] == candidate:
                votes += 1
            else:
                votes -= 1

        return candidate

# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]

print(Solution().majorityElement(nums))