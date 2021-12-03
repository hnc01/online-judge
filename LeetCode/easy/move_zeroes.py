'''
    Accepted
'''

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0

        i = 0

        while i < len(nums):
            if nums[i] == 0:
                # move the next element to this place
                nums.pop(i)
                count_0 += 1

                # here we don't increment the counter because the element we moved in could also be a 0
            else:
                i += 1

        for j in range(0, count_0):
            nums.append(0)

'''
    Accepted: this is the optimal solution suggested by them that takes up only O(1) additional space
'''
class Solution2:
    def moveZeroes(self, nums) -> None:
        lastNonZeroFoundAt = 0

        for cur in range(0, len(nums)):
            if nums[cur] != 0:
                temp = nums[cur]
                nums[cur] = nums[lastNonZeroFoundAt]
                nums[lastNonZeroFoundAt] = temp

                lastNonZeroFoundAt += 1


# list = [0, 1, 0, 0, 3, 12, 16, 1]
list = [0,1,0,3,12]

Solution2().moveZeroes(list)

print(list)
