class Solution:
    '''
        Both accepted
    '''
    def singleNumber(self, nums: list[int]) -> int:
        # we have the unique numbers of the array
        unique_nums = set(nums)

        # if we do x 2 to the sum of the of the unique_nums, we would get the same sum as
        # the original nums but with an extra amount which is the number that unique in original nums
        return (2 * sum(unique_nums)) - sum(nums)

    def efficientSingleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If we take XOR of zero and some bit, it will return that bit
        # If we take XOR of two same bits, it will return 0
        # so if we XOR all the numbers together, eventually the same numbers will do bitwise XOR
        # with each other and cancel out their bits and we'd be left with the bits for the single number

        # Note: if you print the sequence of i and a, it would be like we're doing a "-" (minus) for all the
        # numbers we've already seen
        a = 0

        for i in nums:
            a ^= i

        return a

solution = Solution()
solution.efficientSingleNumber([4,1,2,1,2])