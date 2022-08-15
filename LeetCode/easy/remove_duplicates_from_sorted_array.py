class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        lastSeenNum = nums[0]  # 12

        k = 1  # 3

        for i in range(1, len(nums)):
            j = i  # 3

            while j < len(nums) and nums[j] == lastSeenNum:
                j += 1

            # j = 4
            # j is either >= len(nums) or we found the first element diff than last seen
            if j < len(nums):
                # we found the first element diff than last seen
                # we need to shift the array to the left by j - i
                m = i  # nums[2] = nums[3] =

                while m < len(nums) and (m + j - i) < len(nums):
                    nums[m] = nums[m + j - i]
                    m += 1

                while m < len(nums):
                    nums[m] = nums[m - 1]
                    m += 1

                lastSeenNum = nums[i]
                k += 1
            else:
                # we are done and we return k
                break

        return k