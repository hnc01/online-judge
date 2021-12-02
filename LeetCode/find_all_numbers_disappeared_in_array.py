'''
    Accepted
'''


class Solution:
    def findDisappearedNumbers(self, nums) -> list:
        counts = [0] * (len(nums) + 1)

        for i in nums:
            counts[i] += 1

        result_list = []

        for i in range(1, len(counts)):
            if counts[i] == 0:
                result_list.append(i)

        return result_list
