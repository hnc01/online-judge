'''
    https://leetcode.com/problems/regular-expression-matching/

    10. Regular Expression Matching

    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
        - '.' Matches any single character.
        - '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).
'''

'''
    Accepted
'''


class Solution2:
    def isMatcHelper(self, s, p, s_index, p_index):
        if p_index == len(p) and s_index == len(s):
            # we finished parsing both strings at the same time => we were able to match them
            return True

        elif p_index == len(p) and s_index < len(s):
            # we finished the pattern already but there are still characters in the string
            # since these letters did not fit into our pattern then the pattern doesn't fit the string
            return False

        elif s_index == len(s) and p_index < len(p):
            # the only way this would work is if we have .* (0 or more of this) or letter* (0 or more of this)
            # left in p

            # current_pattern can be . or letter
            current_pattern = p[p_index]

            if (p_index + 1) < len(p):
                next_pattern = p[p_index + 1]

                # next_pattern can be . or letter or *
                if next_pattern == '.' or next_pattern.isalpha():
                    # we need to match s with current_pattern which is letter or . but s is empty
                    return False
                else:
                    # the pattern we're trying to match with s is either .* or letter* and both
                    # work even if s is empty so we need to surpass them to see if we can still match p to s
                    # we do p_index + 2 to skip current_pattern (. or letter) and *
                    return self.isMatcHelper(s, p, s_index, p_index + 2)
            else:
                # we are at the end of p and we need to match
                # s with a letter or . (i.e., with current pattern) but s is empty
                return False
        else:
            s_letter = s[s_index]
            current_pattern = p[p_index]

            if current_pattern == ".":
                if (p_index + 1) < len(p):
                    # we need to get the next_pattern because we have:
                    # (a) [. + letter] OR (b) [. + .] OR (c) [. + *]
                    next_pattern = p[p_index + 1]

                    # for cases (a) and (b) we do the same thing => we consume one letter from s and move on
                    if next_pattern == "." or next_pattern.isalpha():
                        return self.isMatcHelper(s, p, s_index + 1, p_index + 1)
                    else:
                        # we are in case (c) => our pattern is .* => we consume 0 or more of any letter in s
                        # the loop starts by calling recursively with same s_index to mimic consuming 0 letters
                        while s_index <= len(s):
                            # here we do p_index + 2 because we need to skip the current_pattern (letter) and the next_pattern (*)
                            current_match_result = self.isMatcHelper(s, p, s_index, p_index + 2)

                            if current_match_result:
                                return True

                            s_index += 1

                        # if we reached this case and we didn't return any true, then we need to return False
                        return False
                else:
                    # we are in case (d) [. + EOS]
                    # we consume any letter from s and move on
                    return self.isMatcHelper(s, p, s_index + 1, p_index + 1)
            else:
                # current_pattern.isalpha()
                # we need to get the next pattern to see if we have:
                # (a) [letter + letter] OR (b) [letter + .] OR (c) [letter + *] OR (d) [letter + EOS]
                if (p_index + 1) < len(p):
                    # we are in cases (a), (b), or (c)
                    next_pattern = p[p_index + 1]

                    # for cases (a) and (b) we do the same thing => we consume current_pattern and move on
                    if next_pattern == "." or next_pattern.isalpha():
                        # we need to consume one letter and move on but the letter we consume MUST be s_letter
                        if s_letter == current_pattern:
                            return self.isMatcHelper(s, p, s_index + 1, p_index + 1)
                        else:
                            return False
                    else:
                        # case (c) and next pattern is * => letter* => consume 0 or more of letter in current_pattern

                        # to consume 0 letters
                        current_match_result = self.isMatcHelper(s, p, s_index, p_index + 2)

                        if current_match_result:
                            return True
                        else:
                            # here we need to consume 1 or more letters because consuming 0 didn't work
                            while s_index < len(s) and s_letter == current_pattern:
                                # here we do p_index + 2 because we need to skip the current_pattern (letter) and the next_pattern (*)
                                current_match_result = self.isMatcHelper(s, p, s_index + 1, p_index + 2)

                                if current_match_result:
                                    return True

                                s_index += 1

                                if s_index < len(s):
                                    s_letter = s[s_index]

                            # if we reached this case and we didn't return any true, then we need to return False
                            return False
                else:
                    # we are in case (d)
                    # we need to consume one letter and move on but the letter we consume MUST the letter in current_pattern
                    if s_letter == current_pattern:
                        return self.isMatcHelper(s, p, s_index + 1, p_index + 1)
                    else:
                        return False

    def isMatch(self, s: str, p: str) -> bool:
        # we don't need to cater for case where either one is empty because we are guaranteed
        # by the given that their lengths are at least 1.

        return self.isMatcHelper(s, p, 0, 0)


'''
    Same idea except that we make more use of the recursion (no while loops)
    
    Also, in the below approach we take care of current_pattern being letter or . in same condition and we leave the bulk to handling *
    
    More concise and easier to understand
'''


class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        # in this approach, we will recursively call isMatch but after removing parts of s and parts of the pattern
        # so, unlike the first solution where we were checking an index to see if it's out of bounds. Here, we will
        # do the check on the string itself
        if len(p) == 0:
            # if the pattern is empty then the only way we can return true is if s is also empty
            # otherwise we return false
            return len(s) == 0

        # first we need to match s with the first pattern in p (it's always either a . or a letter)
        # in order for is_first_match to be true, we need s to not be empty AND we need the first letter
        # in s to be any letter OR to be the first pattern in p => in other words we need p[0] to be .
        # or p[0] to be s[0]
        is_first_match = (len(s) > 0) and (p[0] == s[0] or p[0] == '.')

        # now we need to see if the next part of the pattern is the start of another pattern or if it's a *
        if len(p) >= 2 and p[1] == '*':
            # here we have 2 options:
            # consider the case where we match 0 letters from s
            # consider the case where we match 1 or more letters from s
            return self.isMatch(s, p[2:]) or (is_first_match and self.isMatch(s[1:], p))
        else:
            # we need to check if is_first_match is true and proceed with checking the rest of s and p
            # we didn't encounter an * so we need to remove one letter from s and one from p
            return is_first_match and self.isMatch(s[1:], p[1:])


# s = "aa"
# p = "a"
#
# s = "aa"
# p = "a*"

# s = "ab"
# p = ".*"

# s = "bcdabcda"
# p = ".*a"

# s = "bcdabcd"
# p = ".*a"

# s = "bcd"
# p = ".*a"

# s = "bcd"
# p = ".*a.*"

# s = "abcd"
# p = ".*a.*"

# s = "bgcal"
# p = ".*a."

# s = "bgcalu"
# p = ".*a."

# s = "aaa"
# p = "a*a"

# s = "ab"
# p = "c*a*ab"

s = "mississippi"
p = "mis*is*ip*."

# s = "a"
# p ="ab*"

# s = 'ab'
# p = 'ab'

# s = "bbbba"
# p = ".*a*a"

# s = "a"
# p = ".*..a*"

print(Solution3().isMatch(s, p))
