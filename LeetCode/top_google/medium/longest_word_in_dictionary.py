'''
    https://leetcode.com/problems/longest-word-in-dictionary/

    720. Longest Word in Dictionary

    Given an array of strings words representing an English Dictionary, return
    the longest word in words that can be built one character at a time by other words in words.

    If there is more than one possible answer, return the longest word with the smallest lexicographical order.
    If there is no answer, return the empty string.
'''

'''
    Accepted
'''


class Solution:
    def longestWord(self, words: [str]) -> str:
        # first we sort the words in descending order of length
        words.sort(key=lambda item: (-len(item), item))

        # then we go over the words in order to see if they can be created
        for word in words:
            prefix = ""
            foundSolution = True

            for char in word:
                prefix += char

                if prefix not in words:
                    foundSolution = False

                    break

            if foundSolution:
                return word

        return ""


print(Solution().longestWord(words=["world", "w", "wo", "wor", "worl"]))
print(Solution().longestWord(words=["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(Solution().longestWord(words=["apple"]))
