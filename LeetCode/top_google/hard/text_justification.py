'''
    https://leetcode.com/problems/text-justification/

    68. Text Justification

    Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters
    and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when
    necessary so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly
    between words, the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left-justified, and no extra space is inserted between words.

    Note:
    - A word is defined as a character sequence consisting of non-space characters only.
    - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    - The input array words contains at least one word.
'''

'''
    Accepted
'''


class Solution:
    def justifyLine(self, line, maxWidth):
        # now every word is in its own location and every space in its own location
        lineArray = line.split(' ')

        if len(lineArray) > 1:
            spacesToAdd = maxWidth - len(line)

            availableSpaceLocations = len(lineArray) - 1

            spacesSplit = [' '] * availableSpaceLocations

            # then using the pigeonhole principle, we do floor(spacesToAdd / availableSpaceLocations) to see the
            # least number of spaces to add in each hole
            leastAmountOfSpaces = spacesToAdd // availableSpaceLocations

            for i in range(0, len(spacesSplit)):
                spacesSplit[i] += ' ' * leastAmountOfSpaces

            # then we place the remainder of spaces from left to right
            remainderSpaces = spacesToAdd - (leastAmountOfSpaces * availableSpaceLocations)

            spaceIndex = 0

            while remainderSpaces > 0:
                spacesSplit[spaceIndex] += ' '
                remainderSpaces -= 1

                spaceIndex = (spaceIndex + 1) % len(spacesSplit)

            result = ""

            for i in range(0, len(lineArray)):
                result += lineArray[i]

                if i < len(spacesSplit):
                    result += spacesSplit[i]

            return result
        else:
            # there's only one word so add spaces to the right
            spacesToAdd = ' ' * (maxWidth - len(line))

            line += spacesToAdd

            return line

    def fullJustify(self, words: [str], maxWidth: int) -> [str]:
        solution = []

        currentWordIndex = 0
        line = ""

        while currentWordIndex < len(words):
            # try to put currentWordIndex in line
            if line == '' or (len(line) < maxWidth and len(line) + 1 + len(words[currentWordIndex]) <= maxWidth):
                # we can add the current word to the line
                if line == '':
                    line += words[currentWordIndex]
                else:
                    line += ' ' + words[currentWordIndex]

                currentWordIndex += 1
            else:
                # we need to start a new line

                # first we justify the line if needed
                if len(line) < maxWidth:
                    line = self.justifyLine(line, maxWidth)

                # then we add it to our solution
                solution.append(line)

                # then we reset to start with new line
                line = ""

        # we might reach this stage without processing the last line
        if line != "":
            if len(line) < maxWidth:
                # for last line, we always just append spaces to the right
                spacesToAdd = ' ' * (maxWidth - len(line))

                line += spacesToAdd

            # then we add it to our solution
            solution.append(line)

        return solution


print(Solution().fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
print(Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
print(Solution().fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
print(
    Solution().fullJustify(words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth=20))
print(Solution().fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6))
