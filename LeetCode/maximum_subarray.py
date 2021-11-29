class Solution:
    '''
        <-- Slow Solution -->

        def get_sums(self, nums: list, start, end):
            sum = 0

            for i in range(start, end + 1):
                sum += nums[i]

            return sum

        def maxSubArray(self, nums: list) -> int:
            target_length = 0

            # set it to the lowest possible value
            largest_sum = float("-inf")

            while target_length <= len(nums):
                # check all the sub-arrays of length target_length
                for i in range(0, len(nums)):
                    if i + target_length < len(nums):
                        sub_array_sum = self.get_sums(nums, i, i + target_length)

                        if sub_array_sum > largest_sum:
                            largest_sum = sub_array_sum

                target_length += 1

            return largest_sum

        <!-- Slow Solution -->
    '''

    def maxSubArrayHelper(self, nums, start_index, end_index):
        # base case is when we have an array of 1 element or 0 elements
        if start_index <= end_index:
            # we need to get the middle index
            mid = int(start_index + (end_index - start_index) / 2)
            left_sum = 0  # sum from start_index to mid-1
            right_sum = 0  # sum from mid + 1 to end_index

            # get the MAX sum of the left subarray
            current_sum = 0

            # IMPORTANT!!
            # we need to do this in reverse order because we need to consider all
            # subarrays of the form nums[i .. mid-1]. For [-2,1,-3,4,*-1*,2,1,-5,4], if we do this in normal order
            # then we would get the subarrays [-2], [-2,1], [-2,1,-3], [-2,1,-3,4],[-2,1,-3,4,-1] => only last subarray contains the mid
            # whereas if we do this in reverse order: [-1], [4, -1], [-3, 4, -1], [1, -3, 4, -1], [-2, 1, -3, 4, -1] => all subarrays contain the mid point
            # -> we need the midpoint because the joint sum needs to be of the form [i .. mid - 1] + mid + [mid + 1 .. j]
            for i in range(mid - 1, start_index - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)

            # get the MAX sum of the right subarray
            current_sum = 0

            for i in range(mid + 1, end_index + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)

            # we now have the MAX sums of the left subarrays and right subarrays as we have them in the current state (this is needed in case 3)
            # we need to recursively get the max sum of the leftsubarrays
            return max(self.maxSubArrayHelper(nums, start_index, mid - 1), self.maxSubArrayHelper(nums, mid + 1, end_index), left_sum + nums[mid] + right_sum)
        else:
            # no solution
            return float("-inf")

    def maxSubArray(self, nums: list) -> int:
        # we can use a divide and conquer strategy
        # there are 3 possible cases:
        # case 1: the solution lies entirely in the left subarray from start_index to mid - 1
        # case 2: the solution lies entirely in the right subarray from mid + 1 to end_index
        # case 3: the solution lies entirely somewhere around the mid index: [center_start_index to mid -1] [mid] [mid + 1 to center_end_index] where center_start_index
        # is greater than start_index and center_end_index is less than end_index
        # => [start_index -> center_start_index -> mid -> center_end_index -> end_index]
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
