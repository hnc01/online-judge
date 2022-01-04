'''
    https://leetcode.com/problems/product-of-array-except-self/

    238. Product of Array Except Self

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.
'''

'''
    Solutions 1 & 2 don't get accepted because they are not O(n) and Solution3 doesn't get accepted because it uses division
'''


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        output = [0] * len(nums)

        for i in range(0, len(nums)):
            current_product = 1

            for j in range(0, len(nums)):
                if i != j:
                    current_product *= nums[j]

            output[i] = current_product

        return output


class Solution2:
    def productExceptSelf(self, nums: [int]) -> [int]:
        output = [1] * len(nums)

        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    output[j] *= nums[i]

        return output


class Solution3:
    def productExceptSelf(self, nums: [int]) -> [int]:
        total_product = 1

        for i in range(0, len(nums)):
            total_product *= nums[i]

        output = [1] * len(nums)

        for i in range(0, len(nums)):
            output[i] = total_product / nums[i]

        return output


'''
    Accepted: we use 2 arrays product_to_the_left and product_to_the_right to save all the products we get
    by traversing the array from left to right and from right to left
'''


class Solution4:
    def productExceptSelf(self, nums: [int]) -> [int]:
        product_to_the_left = [0] * len(nums)
        product_to_the_right = [0] * len(nums)

        product_to_the_left[0] = 1
        product_to_the_right[len(nums) - 1] = 1

        for i in range(0, len(nums) - 1):
            product_to_the_left[i + 1] = nums[i] * product_to_the_left[i]

        for i in range(len(nums) - 1, 0, -1):
            product_to_the_right[i - 1] = nums[i] * product_to_the_right[i]

        output = [0] * len(nums)

        for i in range(0, len(nums)):
            output[i] = product_to_the_left[i] * product_to_the_right[i]

        return output


'''
    Accepted: same as the above approach except that we use the output array as the product_to_the_right array
    since we can calculate product_to_the_left on the fly since we end up traversing the array from left to right
'''


class Solution5:
    def productExceptSelf(self, nums: [int]) -> [int]:
        # product_to_the_left = [0] * len(nums)
        output = [0] * len(nums)

        output[len(nums) - 1] = 1

        for i in range(len(nums) - 1, 0, -1):
            output[i - 1] = nums[i] * output[i]

        product_to_the_left = 1

        for i in range(0, len(nums)):
            output[i] = product_to_the_left * output[i]
            product_to_the_left *= nums[i]

        return output


nums = [1, 2, 3, 4]
# nums = [-1, 1, 0, -3, 3]

print(Solution5().productExceptSelf(nums))
