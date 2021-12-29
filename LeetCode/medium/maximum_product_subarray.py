'''
    https://leetcode.com/problems/maximum-product-subarray/

    152. Maximum Product Subarray

    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.

    A subarray is a contiguous subsequence of the array.
'''

'''
    Accepted mostly but Time Limit Exceeded
'''


class Solution:
    def maxProduct(self, nums: [int]) -> int:
        max_product = float('-inf')

        for i in range(0, len(nums)):
            current_product = 1

            for j in range(i, len(nums)):
                current_product *= nums[j]

                max_product = int(max(max_product, current_product))

        return max_product


'''
    Accepted
    
    Three cases to consider:
    - If we have a list of all positive numbers, then the chain we're looking for is the multiplication of the entire array
    - If we have a zero, then the chain we have so far can't continue because no matter what we do moving after 0, the product will remain 0.
    So, when we encounter a 0, we must reset our chain and start over.
    - If we have a negative number, we shouldn't reset the chain because we might encounter another negative element later on which might
    reverse the sign of the product.
    
    Time complexity : O(N) where NN is the size of nums.
'''


class Solution2:
    def maxProduct(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]  # to keep track of positive chains
        min_so_far = nums[0]  # to keep track of negative chains
        result = max_so_far # ultimately will hold the max product

        for i in range(1, len(nums)):
            # max_so_far can be increased in three ways:
            # - by considering the current element alone (nums[i]): this will cover the case where the current number
            # is preceded by a 0 in which case we need to reset the chain by starting with the current number
            # - by considering the product nums[i] * max_so_far: i.e. by adding the current element to the product we accumulated
            # this is the scenario where we have a positive product and we're adding a positive number to it
            # - by considering the product nums[i] * min_so_far: the only time this is useful is if we have a negative product chain
            # and min_so_far is negative and nums[i] is also negative. This product will then yield a positive number which might
            # be larger than any product we've seen so far

            # min_so_far can be decreased in three ways:
            # - by considering the current element alone (nums[i]): this will cover the case where the current number is negative and is
            # preceded by a zero. This will help us reset the chain while also handling the case of negative numbers.
            # - by considering the product nums[i] * max_so_far: if the current element is negative, then by multiplying it with the max we've
            # seen will yield a very big negative number which should be saved in min_so_far so we can get the change to negate it again in the future.
            # - by considering the product nums[i] * min_so_far: if min_so_far is positive then it means the current number is the first negative
            # one we've seen and will therefore give us the change to negate the negative chain in the future.

            # we need to make sure we don't alter max_so_far before we calculate min_so_far
            temp_max = int(max(nums[i], max_so_far * nums[i], min_so_far * nums[i]))
            min_so_far = int(min(nums[i], max_so_far * nums[i], min_so_far * nums[i]))

            max_so_far = temp_max

            result = int(max(result, max_so_far))

        return result


nums = [2, 3, -2, 4]  # 6
print(Solution().maxProduct(nums))
nums = [-2, 0, -1]  # 0
print(Solution().maxProduct(nums))
nums = [-2, 3, -4]  # 24
print(Solution().maxProduct(nums))
