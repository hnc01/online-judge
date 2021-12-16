'''
    https://leetcode.com/problems/sort-colors/

    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.
'''

'''
    Accepted: Use bubblesort
    
    Runtime: 45 ms, faster than 10.99% of Python3 online submissions for Sort Colors.
    Memory Usage: 14.1 MB, less than 92.14% of Python3 online submissions for Sort Colors.
'''


class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # order: red -> white -> blue
        # 0 = red // 1 = white // 2 = blue

        for i in range(0, len(nums)):
            for j in range(0, len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

'''
    Accepted: Use insertion sort
    
    Runtime: 54 ms, faster than 6.03% of Python3 online submissions for Sort Colors.
    Memory Usage: 14.3 MB, less than 12.77% of Python3 online submissions for Sort Colors.
'''

class Solution2:
    def sortColors(self, nums: [int]) -> None:
        for j in range(1, len(nums)):
            key = nums[j]

            # start from the element before and keep going back
            i = j - 1

            while i >= 0 and nums[i] > key:
                # we need to swap
                nums[i + 1] = nums[i]

                i = i - 1

            nums[i + 1] = key


array = [2,0,2,1,1,0]

Solution2().sortColors(array)

print(array)
