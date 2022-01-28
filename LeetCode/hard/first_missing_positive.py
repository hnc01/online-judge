'''
    https://leetcode.com/problems/first-missing-positive/

    41. First Missing Positive

    Given an unsorted integer array nums, return the smallest missing positive integer.

    You must implement an algorithm that runs in O(n) time and uses constant extra space.
'''

'''
    If the problem statement is that only ONE positive number is missing. The below would have worked.
    But, we could have more than 1 missing positive number and we only need the smallest one.
'''


class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        max_num = 0

        for num in nums:
            if num > max_num:
                max_num = num

        if max_num > 0:
            # we have positive numbers in nums
            # now we xor all the positive numbers in nums
            nums_xored = 0

            for i in range(0, len(nums)):
                if nums[i] > 0:
                    nums_xored ^= nums[i]

            # now we xor all the positive numbers that should be in nums
            positive_xored = 0

            for i in range(1, max_num + 1):
                positive_xored ^= i

            # now we xor the positive numbers in nums with the positive numbers
            # that should be in nums
            xor_result = nums_xored ^ positive_xored

            if xor_result > 0:
                return xor_result
            else:
                # there's no missing number in the range 1 to max_num
                # so the smallest missing number is the next positive number after max_num
                return max_num + 1
        else:
            # all the numbers are negative so the first missing positive is 1
            return 1


'''
    Memory limit exceeded
'''


class Solution2:
    def firstMissingPositive(self, nums: [int]) -> int:
        # first we get min and max from nums
        min_num = float('inf')
        max_num = float('-inf')

        for num in nums:
            if num > 0:
                max_num = int(max(max_num, num))
                min_num = int(min(min_num, num))

        if min_num > 1:
            # if the smallest number in nums is greater than 1
            # then for sure the smallest missing positive num is 1
            return 1
        else:
            # we create an array going from 1 to max_num
            # such that exist[i] is 1 if i is in nums, 0 otherwise.
            exists = [0] * (max_num + 1)

            for num in nums:
                if num > 0:
                    exists[num] = 1

            # now we go through exists from 1 to max_num and see if
            # we can find a number whose exists value is 0
            for i in range(1, len(exists)):
                if exists[i] == 0:
                    return i

            # if we did not return in the above loop it means that all
            # the integers from 1 to max_num are in nums so the smallest
            # missing positive integer is the number after max_num
            return max_num + 1


'''
    Accepted
    
    We loop over the array 2 times in a row => O(2n) = O(n)
    
    We use as extra space the set which holds max all the numbers in nums which is O(n) space
'''


class Solution3:
    def firstMissingPositive(self, nums: [int]) -> int:
        unique_nums = set()

        min_num = 0
        max_num = 0

        for num in nums:
            if num > 0:
                min_num = int(min(min_num, num))
                max_num = int(max(max_num, num))

                unique_nums.add(num)

        # now unique_nums has all the unique positive numbers in nums
        if min_num > 1:
            # if the minimum number in the list is bigger than 1, then for sure
            # the first missing number is 1
            return 1
        else:
            next_min = 1

            while next_min in unique_nums:
                next_min += 1

            return next_min


'''
    Accepted: the below solution is without using extra space like Solution3
    
    Used same trick as find_the_duplicate_number.py in `medium`
'''


class Solution4:
    def firstMissingPositive(self, nums: [int]) -> int:
        # we know that we don't care about 0s or negative numbers
        # also, if we have n elements in the array then we have 2 options:
        # either all the numbers from 1 to n are in the array in which case the minimum missing is n+1
        # some numbers from 1 to n are missing in the array which means the minimum missing is <= n
        # the cases where the missing number is n+1 OR n will be handled separately

        # either way, we don't care about numbers that are greater than n so we can discard them too

        # first let's make sure that 1 is not the missing number
        # Note: the below can be replaced with if 1 in nums return 1 else continue logic
        min_num = float('inf')

        for num in nums:
            if num > 0:
                min_num = int(min(min_num, num))

        if min_num > 1:
            # the first missing number is 1
            return 1
        else:
            # we can proceed with the logic in the above comment
            # first we need to delete all the numbers we don't care about
            # since we can't delete them without ending up with an O(n^2) solution
            # the only way is to mask them. Furthermore, since we already made sure
            # that 1 is not the missing number, then we can mask all these unwanted
            # numbers by replacing them with 1.
            n = len(nums)

            for i in range(0, len(nums)):
                if nums[i] <= 0 or nums[i] > n:
                    nums[i] = 1

            # now all that's left in the array are the numbers we care to check
            # since we have all the elements in nums between 1 and len(nums)
            # then we can use the nums array as a hashmap
            for i in range(0, len(nums)):
                index = int(abs(nums[i]))

                # we are flipping the sign of all the numbers we're seeing
                # so at the end of this, if nums[1] < 0 then 1 is in nums

                # we might have a number in nums that's = n
                # so that we don't go out of range, we will use the index 0 to know if
                # n exists in nums or not (we can use the nums[0] because we don't actually
                # need to index 0 since we remove 0s from the array by replacing them with 1)
                if index == n:
                    if nums[0] > 0:
                        nums[0] *= -1
                else:
                    if nums[index] > 0:
                        nums[index] *= -1

            for i in range(1, len(nums)):
                if nums[i] > 0:
                    return i

            # none of the numbers from 1 to n-1 are missing
            # the only options left are if n is missing or n+1

            if nums[0] > 0:
                # nums[0] is not negative so n is not not among the numbers from 1 to n in nums
                return n
            else:
                # we have n in nums so the first missing is n+1
                return n + 1


# nums = [1, 2, 0]
# nums = [3, 4, -1, 1]
nums = [7, 8, 9, 11, 12]
# nums = [1]

print(Solution4().firstMissingPositive(nums))
