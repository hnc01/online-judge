'''
    https://leetcode.com/problems/subarray-sum-equals-k/

    560. Subarray Sum Equals K

    Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
'''

'''
    Accepted by Time Limit Exceeded
'''


class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        count = 0

        for i in range(0, len(nums)):
            subarray_sum = nums[i]

            if subarray_sum == k:
                count += 1

            j = i + 1

            # starting at an index, we can have more than one subarrays leading to target k
            # for example, [1,-1,0], if we start at index 0 we can have [1,-1] which gives 0 and [1,-1,0] which also gives 0
            # so at index 0, we can have 2 subarrays that give us target k
            while j < len(nums):
                subarray_sum += nums[j]

                if subarray_sum == k:
                    count += 1

                j += 1

        return count


'''
    I got memory limit exceeded. However, I need to keep in mind that I don't need to entire matrix of sums. All I need is the previous row.
    So, instead of savings the entire matrix of sums, I'll just keep in memory the last row while computing a new row of sums.
    Check Solution3.
'''


class Solution2:
    def subarraySum(self, nums: [int], k: int) -> int:
        # we will make use of a matrix of sums which will accumulate all sums sum[i][j] for i,j in [0, len(nums)[ st i <= j
        # the indices in the matrix of sums will be from 0 to len(nums)
        sums = [[]] * len(nums)

        for i in range(0, len(nums)):
            sums[i] = [0] * len(nums)

        count = 0

        # first we'll fill the diagonal of the matrix i.e., sums[i][i]
        for i in range(0, len(nums)):
            sums[i][i] = nums[i]

            if sums[i][i] == k:
                count += 1

        # now we start incrementally building our sums matrix
        # the first row of the matrix will be built alone and then we'll loop to build the rest of it

        for i in range(1, len(nums)):
            sums[0][i] = sums[0][i - 1] + nums[i]

            if sums[0][i] == k:
                count += 1

        # now we're done with the first row, we will build the rest using a loop

        # we loop over rows from 1 to len(nums) - 1 (because we already did row 0)
        for row in range(1, len(nums)):
            # we want to fill the right side of the matrix (right side of diagonal) only
            # utilizing the cells that are right of the diagonal would mean we're adding numbers
            # together that don't form a subarray
            for col in range(row + 1, len(nums)):
                sums[row][col] = sums[row - 1][col] - nums[row - 1]

                if sums[row][col] == k:
                    count += 1

        return count


'''
    Attempting to get accepted by saving only the latest row of sums in memory.
    
    Still time limit exceeded. Need to find a solution that's O(n).
'''


class Solution3:
    def subarraySum(self, nums: [int], k: int) -> int:
        # we will make use of a matrix of sums which will accumulate all sums st sums[i] = sum of all the elements from 0 to i
        previous_row = [0] * len(nums)

        # if the first element is equal to target then we automatically found our first result (since we won't be revisiting sums[0])
        # so we start our count with 1, otherwise we start at 0.
        if nums[0] == k:
            count = 1
        else:
            count = 0

        # we set the sum[0] (i.e., sum from 0 to 0) to be the first element
        previous_row[0] = nums[0]

        # now we're filling the sums array with all the sums from 0 to i where i in [0, len(nums)-1]
        for i in range(1, len(nums)):
            previous_row[i] = previous_row[i - 1] + nums[i]

            if previous_row[i] == k:
                count += 1

        # now we're done with the first row, we will build the rest using a loop
        # we'll use previous row to build current row
        row = 1
        current_row = [0] * len(nums)

        while row < len(nums):
            for col in range(row, len(nums)):
                current_row[col] = previous_row[col] - nums[row - 1]

                if current_row[col] == k:
                    count += 1

            previous_row = current_row.copy()
            current_row = [0] * len(nums)

            row += 1

        return count


'''
    Accepted!
    
    The idea behind the below solution is that we go through the nums array 2 times but not in a nested way.
    
    The first time we go through the array is to accumulated the sums from 0 to i where i goes from 0 to len(nums) - 1.
    This array of sums is the only one we'll need to get all the other sums from j to len(nums)-1 because all we have to do
    is subtract the elements from 0 to j-1 from the accumulated sums to get the sums at j. 
    
    The second time we go through the array, we first make sure to record the sum of all the numbers we've already examined (I save
    the sum in prev_elements_sum) and we also make sure to reduce the number of times we see a sum since with every iteration we want
    to ignore the elements and sums that are before our current index. To know which target to look for in the original sums array,
    we do target_number = k + prev_elements_sum. Why? because we want to look for a number in the original sum, such that if we remove
    from it all the numbers we've seen so far (i.e. thereby getting the sums of current elements), we'd get k. We keep track of the
    count of sums in our sums array to make sure the look up for target_number is fast and we make sure to update the row_0_sums_count
    correctly at the start of each iteration so the counts stay correct.
'''


class Solution4:
    def subarraySum(self, nums: [int], k: int) -> int:
        # let's first build the sums from 0 to len(nums) - 1
        # we will make use of a matrix of sums which will accumulate all sums st sums[i] = sum of all the elements from 0 to i
        row_0_sums = [0] * len(nums)
        row_0_sums_count = {}

        # if the first element is equal to target then we automatically found our first result (since we won't be revisiting sums[0])
        # so we start our count with 1, otherwise we start at 0.
        if nums[0] == k:
            count = 1
        else:
            count = 0

        # we set the sum[0] (i.e., sum from 0 to 0) to be the first element
        row_0_sums[0] = nums[0]
        row_0_sums_count[nums[0]] = 1

        # now we're filling the sums array with all the sums from 0 to i where i in [0, len(nums)-1]
        for i in range(1, len(nums)):
            row_0_sums[i] = row_0_sums[i - 1] + nums[i]

            if row_0_sums[i] in row_0_sums_count:
                row_0_sums_count[row_0_sums[i]] += 1
            else:
                row_0_sums_count[row_0_sums[i]] = 1

            if row_0_sums[i] == k:
                count += 1

        # so far we made one pass over the array
        # now we loop over nums again only once and we accumulate sum information along the way to help us solve the problem

        # this will hold the sum of all the elements we've already explored
        prev_elements_sum = nums[0]

        for i in range(1, len(nums)):
            # first we need to decrement the number of times we see row_0_sums[i-1] because we effectively ignoring all elements before i
            row_0_sums_count[row_0_sums[i - 1]] -= 1

            # in order to get target sum for current_number, we need to have k + prev_elements_sum in row_0_sums.
            target_number = k + prev_elements_sum

            # check to see how many times target_number appears in our list of sums
            if target_number in row_0_sums_count and row_0_sums_count[target_number] > 0:
                count += row_0_sums_count[target_number]

            prev_elements_sum += nums[i]

        return count


# nums = [1, 1, 1]
# k = 2

# nums = [1,2,3]
# k = 3

# nums = [1]
# k = 0

# nums = [1, -1, 0]
# k = 0

nums = [1, -1, 0, 3, 2, -5, 1]
k = 0

print(Solution4().subarraySum(nums, k))
