'''
    https://leetcode.com/problems/find-and-replace-in-string/

    833. Find And Replace in String

    You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations
    are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

    To complete the ith replacement operation:
        - Check if the substring sources[i] occurs at index indices[i] in the original string s.
        - If it does not occur, do nothing.
        - Otherwise if it does occur, replace that substring with targets[i].

    For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

    All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other.
    The testcases will be generated such that the replacements will not overlap.
        - For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab"
        and "bc" replacements overlap.

    Return the resulting string after performing all replacement operations on s.

    A substring is a contiguous sequence of characters in a string.
'''

import collections

'''
    Accepted
'''


class Solution:
    def findReplaceString(self, s: str, indices: [int], sources: [str], targets: [str]) -> str:
        replacements = {}

        for i in range(0, len(indices)):
            startIndex = indices[i]
            source = sources[i]
            target = targets[i]

            # check if s[startIndex:startIndex+len(source)] == source
            if (startIndex + len(source)) <= len(s):
                # it means that the substring is valid
                if s[startIndex:startIndex + len(source)] == source:
                    # the replacement is valid so we can add it to our listen of replacements
                    replacements[startIndex] = (startIndex, source, target)

        # now we have only valid moves + they are ordered by indices
        replacements = collections.OrderedDict(sorted(replacements.items()))

        for originalIndex in replacements:
            index, source, target = replacements[originalIndex]

            # perform the replacement on s
            s = s[0:index] + target + s[index + len(source):]

            # now we need offset all the indices that are greater than originalIndex with len(target) - len(source) (could be negative)
            for key in replacements:
                if key > originalIndex:
                    replacements[key] = (replacements[key][0] + len(target) - len(source), replacements[key][1], replacements[key][2])

        return s


print(Solution().findReplaceString(s="abcd", indices=[2, 0], sources=["cd", "a"], targets=["ffff", "eee"]))
print(Solution().findReplaceString(s="abcd", indices=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]))
