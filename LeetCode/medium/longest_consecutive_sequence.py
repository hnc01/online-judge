'''
    https://leetcode.com/problems/longest-consecutive-sequence/

    128. Longest Consecutive Sequence

    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.
'''

'''
    Time limit exceeded
'''


class Solution:
    def is_consecutive(self, n, group):
        return n + 1 in group or n - 1 in group

    def longestConsecutive(self, nums: [int]) -> int:
        groups = []

        for num in nums:
            to_merge = []
            singles = []

            for group in groups:
                if self.is_consecutive(num, group):
                    to_merge = to_merge + list(group)
                else:
                    singles.append(group)

            to_merge.append(num)

            groups = []

            groups += singles
            groups.append(set(to_merge))

        max_length = 0

        for group in groups:
            max_length = int(max(max_length, len(group)))

        return max_length


'''
    In this approach, for each number, we build the sequence left and right and stop when we can't find any of the numbers
    in the given array
'''


class Solution2:
    def longestConsecutive(self, nums: [int]) -> int:
        groups = []
        visited = set()

        nums = set(nums)

        for num in nums:
            if num not in visited:
                group = set()

                group.add(num)

                # get all the available sequences of this number
                # we go left and we go right
                left = num - 1
                right = num + 1

                while left in nums:
                    visited.add(left)
                    group.add(left)
                    left -= 1

                while right in nums:
                    visited.add(right)
                    group.add(right)
                    right += 1

                groups.append(group)

        max_length = 0

        for group in groups:
            max_length = int(max(max_length, len(group)))

        return max_length


'''
    Same approach as Solution 2 but we don't wait until the end to get the max_length
'''


class Solution3:
    def longestConsecutive(self, nums: [int]) -> int:
        visited = set()

        nums = set(nums)

        max_length = 0

        for num in nums:
            if num not in visited:
                group = set()

                group.add(num)

                # get all the available sequences of this number
                # we go left and we go right
                left = num - 1
                right = num + 1

                while left in nums:
                    visited.add(left)
                    group.add(left)
                    left -= 1

                while right in nums:
                    visited.add(right)
                    group.add(right)
                    right += 1

                max_length = int(max(max_length, len(group)))

        return max_length


print(Solution2().longestConsecutive([]))
