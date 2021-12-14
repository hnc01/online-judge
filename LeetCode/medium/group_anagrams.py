'''
    https://leetcode.com/problems/group-anagrams/

    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''


class Solution:
    # Note: using XOR doesn't work in this case because equal letters in the same string could cancel out each other
    # even if they dont even exist in the second string

    # def is_anagram(self, first_string, second_string):
    #     if len(first_string) != len(second_string):
    #         return False
    #     else:
    #         combined = []
    #
    #         for i in range(0, len(first_string)):
    #             combined.append(ord(first_string[i]))
    #             combined.append(ord(second_string[i]))
    #
    #         result = 0
    #
    #         for i in range(0, len(combined)):
    #             result ^= combined[i]
    #
    #         return result == 0

    # Note: this takes too long because we need to examine each letter separately and create an array for each
    # which needs too much memory

    # def is_anagram(self, first_string, second_string):
    #     if len(first_string) != len(second_string):
    #         return False
    #     else:
    #         first_string_arr = [0] * 26
    #         second_string_arr = [0] * 26
    #
    #         for i in range(0, len(first_string)):
    #             first_string_arr[ord(first_string[i]) - 97] += 1
    #             second_string_arr[ord(second_string[i]) - 97] += 1
    #
    #         return first_string_arr == second_string_arr

    # Note: since the length of each string is max 100, we can afford to sort the letters and make the solution easy
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        groups = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string in groups:
                groups[sorted_string].append(string)
            else:
                groups[sorted_string] = [string]

        return list(groups.values())


strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))
