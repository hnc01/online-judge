'''
    https://leetcode.com/problems/rotate-array/

    189. Rotate Array

    Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

'''
    Correct but time Limit Exceeded (this is brute force approach in solution)
'''


class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for t in range(0, k):
            # shift the array once to the right
            carry = nums[0]

            for i in range(1, len(nums)):
                # shift the current element to the right
                temp = nums[i]
                nums[i] = carry
                carry = temp

            # finally we swap the last element with first
            nums[0] = carry


'''
    Accepted but takes O(N) extra space. Challenge is to do it in O(1) extra space.
'''


class Solution2:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        old_nums = nums.copy()

        for i in range(0, len(nums)):
            new_index = int((i + k) % len(nums))

            # place old_nums[i] in nums[new_index]
            nums[new_index] = old_nums[i]


'''
    Accepted
    
    We compute the replacements as we go along jumping from one place to the next keeping track of how many shifts we've made
'''


class Solution3:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shifts_count = 0  # needs to reach len(nums)
        index_to_shift = 0
        carry = nums[index_to_shift]
        start_cycle_index = 0

        while shifts_count < len(nums):
            # we need to compute the shifted index
            new_index = (index_to_shift + k) % len(nums)
            # swapping between previous element and current
            temp = nums[new_index]
            nums[new_index] = carry
            carry = temp

            index_to_shift = new_index

            shifts_count += 1

            if new_index == start_cycle_index:
                # we ended up where we started
                start_cycle_index += 1

                if start_cycle_index >= len(nums):
                    # no more cycles to consider so we break the loop
                    break

                index_to_shift = start_cycle_index
                # in this case we don't have a carry so we need
                # to reset the cycle by resetting the start index and the carry
                # just like at the beginning how we set carry to be first element
                carry = nums[start_cycle_index]


# same approach as above but reduced k to smaller number by eliminating the rotations that would make
# nums just go back to how its original value
class Solution4:
    def rotate(self, nums: [int], k: int) -> None:
        # no need to perform any changes because shifting the array
        # by its length will result in the same array
        if k == len(nums):
            return

        # next, we need to remove from the number of rotations that would
        # just lead to nums getting back to nums => all the len(nums) out of k
        if k > len(nums):
            k = k % len(nums)

        # the idea now is that we need to compute where each index will end up
        # also, we're sure that we need to make n replacements because we need
        # shift every element k places

        indexToShift = 0
        valueToShift = nums[0]

        startCycleIndex = 0

        n = len(nums)

        shiftedElementsCount = 0

        while shiftedElementsCount < n:
            destinationIndex = (indexToShift + k) % n

            # we need to put valueToShift in destinationIndex
            valueToShift, nums[destinationIndex] = nums[destinationIndex], valueToShift

            indexToShift = destinationIndex

            shiftedElementsCount += 1

            if destinationIndex == startCycleIndex:
                # we ended up where we started
                # so we need to start at the next element from where we started
                startCycleIndex += 1

                if startCycleIndex >= len(nums):
                    # no more cycles to consider so we break the loop
                    break

                indexToShift = startCycleIndex
                # in this case we don't have a carry so we need
                # to reset the cycle by resetting the start index and the carry
                # just like at the beginning how we set carry to be first element
                valueToShift = nums[startCycleIndex]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

nums = [-1, -100, 3, 99]
k = 2

Solution3().rotate(nums, k)
print(nums)
