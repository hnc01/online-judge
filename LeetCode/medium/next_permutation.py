'''
    https://leetcode.com/problems/next-permutation/

    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

    If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

    The replacement must be in place and use only constant extra memory.
'''

'''
    Accepted
    
    General Idea:
    As long as the next element is greater than anything we've ever seen, all we need to do is sort the array because it means
    we need to abide by the question and present the 'lowest possible order' in such a case and so we sort in asc order.
    When we find the next element is less than an element we've already seen, it means that this is the element we need to replace
    with something higher because its current combination is the max possible. So, we swap it with the next largest element among
    the elements we've already seen (note that the resulting array after the current element would still remain sorted because we
    swapped the current element with the one that comes directly after it).
'''


class Solution:
    def find_max(self, nums, start, pivot):
        for i in range(start, len(nums)):
            if nums[i] > pivot:
                return i

        return -1

    def sort_nums(self, nums, start):
        for i in range(start, len(nums)):
            for j in range(i, len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

    def nextPermutation(self, nums) -> None:
        if len(nums) > 1:
            # goes from len(nums)-1 to 1
            for i in range(len(nums) - 2, -1, -1):
                max_index = self.find_max(nums, i + 1, nums[i])

                '''
                    The only different between my solution and theirs is that i keep the array sorted at each step
                    while their solution only sorts after we do the swap (they reverse because when we don't find i-1 < i
                    it means the array is already sorted in desc order and all we need to do is reverse it)
                '''
                if max_index == -1:
                    # sort in ascending
                    self.sort_nums(nums, i)
                    # max index is always the last element in the array
                elif nums[i] < nums[max_index]:
                    # swap between max_index and i and we're done
                    temp = nums[i]
                    nums[i] = nums[max_index]
                    nums[max_index] = temp

                    break


nums = [1]

Solution().nextPermutation(nums)

print(nums)
