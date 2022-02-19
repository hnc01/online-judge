'''
    https://leetcode.com/problems/sentence-screen-fitting/

    418. Sentence Screen Fitting

    Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given
    sentence can be fitted on the screen.

    The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two
    consecutive words in a line.
'''

'''
    Accepted but time limit exceeded
    
    We notice that at some point we're just repeating the same pattern of placing the sentence in the rows
    So maybe we need to find a pattern where we fully place the sentence (one or more times) and see how many
    times this pattern can be repeated
'''


class Solution:
    def wordsTyping(self, sentence: [str], rows: int, cols: int) -> int:
        # first we do a check to see if all words have length less than our number of cols
        # if we find a word whose length is > cols, it means that we can't fit that word no matter what
        # so the number of solutions is 0
        for word in sentence:
            if len(word) > cols:
                return 0

        # to keep track of the number of times we successfully place the full sentence
        count = 0

        # we will use i to loop over the words in sentence
        i = 0

        for r in range(0, rows):
            # we will use c to keep track of the column we're at when we're in row r
            c = 0

            while c < cols:
                # check if sentences[i] can fit in current row starting at col c
                if (cols - c) >= len(sentence[i]):
                    # if the remaining number of cols in row can fit sentence[i]
                    # we add it by increasing c by len(sentence) + 1 to account for
                    # the space between 2 consecutive words
                    c += len(sentence[i]) + 1

                    # we increase i to place the next word
                    i += 1

                    if i >= len(sentence):
                        # we successfully placed all the words once
                        count += 1
                        i = 0
                else:
                    # try to place current word in next (empty) row
                    break

        return count


'''
    Accepted
'''


class Solution2:
    def wordsTyping(self, sentence: [str], rows: int, cols: int) -> int:
        # first we do a check to see if all words have length less than our number of cols
        # if we find a word whose length is > cols, it means that we can't fit that word no matter what
        # so the number of solutions is 0
        for word in sentence:
            if len(word) > cols:
                return 0

        # to keep track of patterns => if 2 patterns are equivalent it means they start and end with same word
        # we won't save the word itself because there could be duplicates => we'll save the indices of the words
        first_to_last_word_index_map = {}

        # maps each index where a pattern starts to the number of times the sentence appears in full in the pattern
        pattern_sentence_count = {}

        # we will use i to loop over the words in sentence
        i = 0

        for r in range(0, rows):
            # we will use c to keep track of the column we're at when we're in row r
            c = 0

            # keep track of the first word of this pattern
            first_word_index = i

            # we check the first word we're going to insert in this pattern
            if first_word_index in first_to_last_word_index_map:
                # we've already seen this pattern so we break because now we're repeating
                break
            else:
                # we insert the first word in the list of patterns
                first_to_last_word_index_map[first_word_index] = -1
                pattern_sentence_count[first_word_index] = 0

                while c < cols:
                    # check if sentences[i] can fit in current row starting at col c
                    if (cols - c) >= len(sentence[i]):
                        # if the remaining number of cols in row can fit sentence[i]
                        # we add it by increasing c by len(sentence) + 1 to account for
                        # the space between 2 consecutive words
                        c += len(sentence[i]) + 1

                        # constantly update the last word we see in pattern
                        first_to_last_word_index_map[first_word_index] = i

                        # we increase i to place the next word
                        i += 1

                        if i >= len(sentence):
                            # we successfully placed all the words once

                            # update the pattern count
                            pattern_sentence_count[first_word_index] += 1

                            # reset the sentence index
                            i = 0
                    else:
                        # try to place current word in next (empty) row
                        break

        # now we follow the patterns by starting with first word in sentence as the first word pattern
        current_word_index = 0

        # keep track of the number of times the full sentence was repeated
        count = 0

        # now repeatedly follow the pattern until we're done with the number of rows
        for r in range(0, rows):
            # number of times the full sentence appears with pattern starting with index 0
            count += pattern_sentence_count[current_word_index]

            # the next word is the word after the last word in the current pattern
            next_word_index = first_to_last_word_index_map[current_word_index]

            if next_word_index == len(sentence) - 1:
                next_word_index = 0
            else:
                next_word_index += 1

            current_word_index = next_word_index

        return count


# print(Solution2().wordsTyping(sentence=["hello", "world"], rows=2, cols=8))
# print(Solution2().wordsTyping(sentence=["a", "bcd", "e"], rows=3, cols=6))
# print(Solution2().wordsTyping(sentence=["i", "had", "apple", "pie"], rows=4, cols=5))
print(Solution2().wordsTyping(["hi", "ho", "ni", "hao", "la", "night", "leetcode", "welcome", "awesome", "light"], 10000, 333))
# print(Solution2().wordsTyping(["a"], 10000, 10000))
# print(Solution2().wordsTyping(["a"], 10, 10))
# print(Solution2().wordsTyping(["ni", "hao", "wo", "hen", "hao"], 10, 22))
