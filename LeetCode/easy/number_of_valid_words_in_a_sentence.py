import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(" ")

        validWordPattern = re.compile("^([a-z])*([a-z]+-[a-z]+)?([a-z])*([!\\.,])?$")

        count = 0

        for word in words:
            # we strip just in case we have any trailing spaces so we
            # don't process such tokens
            word = word.strip()

            if len(word) > 0:
                # it's not an empty string and not a string of spaces
                if validWordPattern.match(word) is not None:
                    count += 1

        return count