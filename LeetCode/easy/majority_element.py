'''
    Solution 1 [Accepted]: this solution runs in O(n) time but it requires O(n) of additional space to save the numbs_count dict
'''
class Solution1:
    def majorityElement(self, nums: list) -> int:
        nums_counts = {}

        for nb in nums:
            if nb in nums_counts:
                nums_counts[nb] += 1
            else:
                nums_counts[nb] = 1

            # immediately once we find an element who's a majority, we return it
            if nums_counts[nb] > int(len(nums) / 2):
                return nb

'''
    Solution 2 [Accepted]: `Boyer-Moore Voting Algorithm` suggested by solution manual of leetcode
    The idea is that we virtually dissect our array in a way where our candidate for highest frequency is always at the beginning of each section.
    Every time we see a value equal to our candidate we increment the counter and every time we see a value different from our candidate we decerement
    the counter. Whenever the counter resets to 0, it means that we found the same number of elements in this section that are different than the candidate
    as much as we had values of candidate; since this section of the array amounts to 0, we can discard it and move on to other sections. Eventually, we should
    reach a section that ends with count > 0, such a section would have the majority element at the beginning of it.
'''
class Solution2:
    def majorityElement(self, nums: list) -> int:
        # count to maintain votes of current section
        count = 0
        # we start with candidate as the first element
        candidate = nums[0]

        for i in range(0, len(nums)):
            if count == 0:
                # time to reset (we don't need to reset count to 0 because it's already equal to 0)
                candidate = nums[i]

            if nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate