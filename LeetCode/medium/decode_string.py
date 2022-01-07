'''
    https://leetcode.com/problems/decode-string/

    394. Decode String

    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square
    brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
    For example, there will not be input like 3a or 2[4].
'''

import re


class Solution:
    def decode_string_helper(self, s):
        if s == "":
            return ""

        if s.isalpha():
            # nothing to do with this substring
            return s

        # we have a full string here and only ONE full string
        pattern = re.compile('([a-z]*)([0-9]+)(\[.*\])([a-z]*)')

        matches = pattern.findall(s)[0]

        prefix = matches[0]
        frequency = int(matches[1])
        substring = matches[2][1:-1]  # removing first and last brackets
        suffix = matches[3]

        substring_result = self.decodeString(substring)

        return prefix + str(frequency * substring_result) + suffix

    def decodeString(self, s: str) -> str:
        if s == "":
            return ""

        if s.isalpha():
            # nothing to do with this substring
            return s

        # let's try to split the string into sections where each one makes up a full substring
        parentheses_stack = []

        final_result = ""
        substring = ""

        entered = False

        for char in s:
            substring += char

            if char == '[':
                entered = True
                parentheses_stack.append(char)
            elif char == ']':
                parentheses_stack.pop()

            if len(parentheses_stack) == 0 and entered:
                # if we popped all of the parentheses it means we have a full substring
                substring_result = self.decode_string_helper(substring)

                final_result += substring_result

                substring = ""
                entered = False

        if substring:
            final_result += substring

        return final_result


# s = "3[a]2[bc]"
# s = "3[a2[c]]"
# s = "3[3[c]a2[cd]]2[a]"
# s = "2[abc]3[cd]ef"
# s = "a3[z]bnc2[bc]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
# s = "2[2[y]pq4[2[jk]e1[f]]]ef"
print(Solution().decodeString(s))
