'''
    https://leetcode.com/problems/longest-string-chain/

    1048. Longest String Chain

    You are given an array of words where each word consists of lowercase English letters.

    wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing
    the order of the other characters to make it equal to wordB.
        - For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

    A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2,
    word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

    Return the length of the longest possible word chain with words chosen from the given list of words.
'''

'''
    Accepted
'''


class Solution:
    def isPredecessor(self, a: str, b: str):
        # in order for a to be a predecessor of b, first len(b) == len(a) + 1
        if len(b) != len(a) + 1:
            return False

        # since len(b) and len(a) are valid, we can proceed with testing out the strings
        if a == b:
            # a is not a predecessor of b because they are equal
            return False

        # we'll use i to loop over a and j for b
        i, j = 0, 0

        nonMatchingLetters = 0

        while i < len(a) and j < len(b):
            # there has to be only one character in a that is not inline with its counterpart in b
            if a[i] == b[j]:
                # we have matching pair so we proceed
                i += 1
                j += 1
            else:
                nonMatchingLetters += 1
                # this could be the letter we added in b so we only progress in b
                j += 1

        if nonMatchingLetters == 0:
            # we exited the while loop without entering in the else
            # it means that everything in a was matched => which means that the extra letter in b is at the end
            return True
        else:
            # if the number of non-matching letters is bigger than 1 then there's more than 1 character difference
            # between a and b so a is not predecessor of b
            return nonMatchingLetters == 1

    def longestStrChain(self, words: [str]) -> int:
        # this will keep track of the length of the longest chain
        # the minimum maxLength would be 1 since we always have at least 1 word in our list
        maxLength = 1

        # first, let's sort the words based on their length in ascending order
        words.sort(key=lambda s: len(s))

        # then, we go in reverse order and for each index, we note the longest chain start at the index
        # by default, the longest chain at each index is the word itself only
        longestChains = [1] * len(words)

        # we start with len(words) -2 because the last word in words by default will remain
        # max length of chain is 1 because there are no other words after it
        for i in range(len(words) - 2, -1, -1):
            a = words[i]

            # find the next word in the chain starting at firstWord
            for j in range(i + 1, len(words)):
                b = words[j]

                if self.isPredecessor(a, b):
                    # we found the next word in the chain so
                    # longestChains[i] = longestChains[j] + 1
                    longestChains[i] = max(longestChains[i], longestChains[j] + 1)

                    maxLength = max(maxLength, longestChains[i])

                    # even though we found a predecessor, we need to process
                    # all predecessor to make sure that we link the current word to next
                    # predecessor that produces the longer chain

        return maxLength


print(Solution().longestStrChain(words=["bdca", "a", "b", "ba", "bca", "bda"]))
print(Solution().longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(Solution().longestStrChain(words=["abcd", "dbqca"]))
print(Solution().longestStrChain(words=["a", "ab", "ac", "bd", "abc", "abd", "abdd"]))
