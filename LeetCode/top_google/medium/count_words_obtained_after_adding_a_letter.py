'''
    https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

    You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

    For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation
    on it to be equal to that from targetWords.

    The conversion operation is described in the following two steps:
        - Append any lowercase letter that is not present in the string to its end.
        For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting
        string will be "abcd".
        - Rearrange the letters of the new string in any arbitrary order.
        For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.

    Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

    Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing
    the operations. The strings in startWords do not actually change during this process.
'''

'''
    Accepted
'''


class Solution:
    def wordCount(self, startWords: [str], targetWords: [str]) -> int:
        # counts the number of targetWords that can be created out of words in startWords using the append or rearrange operations.
        count = 0

        # in order to efficiently test the "shuffle" operation as an option, it's best to sort all of the words
        # in startWords in advance. Each word has a limit of 26 characters so this sorting should be O(N) where N is
        # the number of words in startWords
        sortedStartWords = set()

        for word in startWords:
            sortedStartWords.add("".join(sorted(word)))

        # now that everything is ready, we can start with the solution
        for targetWord in targetWords:
            # we need to see if we can transform any word in startWords to obtain targetWord

            # the first operation is to append a unique character to the end of a startWord to obtain targetWord
            # we start by removing the unique characters in targetWord one by one to see if we can find a sorted version
            # of the remainder of the string in startWords
            uniqueCharacters = set()

            for char in targetWord:
                if char not in uniqueCharacters:
                    uniqueCharacters.add(char)

            # now that we have all the unique characters in targetWord, we remove them one by one
            for char in uniqueCharacters:
                newTargetWord = targetWord[0:targetWord.find(char)] + targetWord[targetWord.find(char) + 1:]
                newTargetWord = "".join(sorted(newTargetWord))

                # now we check if newTargetWord in the sorted start words
                if newTargetWord in sortedStartWords:
                    # this means that by adding a random character to sortedStartWord not in the string already and then shuffling
                    # we can obtain the original targetWord
                    count += 1
                    # if there are more than one way to obtain targetWord, we don't need to count them all
                    break

        return count


print(Solution().wordCount(startWords=["ant", "act", "tack"], targetWords=["tack", "act", "acti"]))
print(Solution().wordCount(startWords=["ab", "a"], targetWords=["abc", "abcd"]))
print(Solution().wordCount(["mox", "bj", "rsy", "jqsh"], ["trk", "vjb", "jkr"]))
