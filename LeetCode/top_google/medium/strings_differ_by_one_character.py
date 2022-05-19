'''
    https://leetcode.com/problems/strings-differ-by-one-character/

    1554. Strings Differ by One Character

    Given a list of strings dict where all the strings are of the same length.

    Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.
'''

'''
    Brute force approach (time limit exceeded)
'''


class Solution:
    def differByOne(self, dict: [str]) -> bool:
        for i in range(0, len(dict)):
            current_word = dict[i]

            for j in range(i + 1, len(dict)):
                other_word = dict[j]

                # check how many differences are there between current_word and other_word
                count_diff = 0

                for c in range(0, len(current_word)):
                    if current_word[c] != other_word[c]:
                        count_diff += 1

                    if count_diff >= 2:
                        # we already exceeded our limit, we don't need to keep processing the word
                        break

                if count_diff == 1:
                    # we found 2 words that have 1 character difference so we return true
                    return True

                # otherwise we move on to other pairs of words

        # if we reach this point, it means we never returned true => no pairs found
        return False

class Solution2:
    def differByOne(self, dict: [str]) -> bool:
        # Observation: if the strings differ by 1 then taking out that 1 character should make them equal
        # we have to loop over each character index, remove that character, and see which strings are rendered equal
        # we can quickly test for equality by adding the strings (after removing character at index) into a set

        m = len(dict[0]) # length of each word in dict => character loop

        for char_index in range(0, m):
            words = set()

            for word in dict:
                # remove the character at char_index
                word = word[0:char_index] + word[char_index+1:]

                if word in words:
                    # we found an existing word that's equal to current word after removing char at char_index
                    return True

                words.add(word)

        # if we reached this point, it means we never returned True => didn't find a pair
        return False


print(Solution2().differByOne(["abcd","acbd", "aacd"]))
print(Solution2().differByOne(["ab","cd","yz"]))
print(Solution2().differByOne(["abcd","cccc","abyd","abab"]))