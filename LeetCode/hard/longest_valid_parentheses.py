'''
    https://leetcode.com/problems/longest-valid-parentheses/

    32. Longest Valid Parentheses

    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

'''
    Accepted but Time Limit Exceeded.
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest_substring = 0

        for i in range(0, len(s)):
            # we need to find the longest substring of valid parenthesis starting at i
            i_longest_substring = 0
            acc_substring_length = 0
            stack = []

            for j in range(i, len(s)):
                if s[j] == "(":
                    stack.append("(")
                else:
                    # we need to pop a (
                    if len(stack) > 0:
                        # we are popping an ( when seeing ) so that's 2 extra characters added to our substring
                        stack.pop()
                        acc_substring_length += 2

                        if len(stack) == 0:
                            # we popped a perfect set of valid parentheses
                            i_longest_substring += acc_substring_length
                            acc_substring_length = 0
                    else:
                        # invalid parenthesis structure so we need to move on to next starting index
                        break

            longest_substring = int(max(longest_substring, i_longest_substring))

        return longest_substring


'''
    Accepted: the idea is that we turn all the valid parentheses substrings into index ranges, and then
    we merge the ranges if they overlap or are adjacent. This will lead to a new list of merged ranges which
    we'll also need to keep merging until we get a set of non-overlapping ranges. These ranges now represent
    all our substrings of valid parentheses. All we need to do at the end is check the lengths of the ranges
    and return the longest one.
'''


class Solution2:
    def mergeIfOverlapping(self, first, second):
        # first we need to make sure that first starting index is less second starting index
        if first[0] > second[0]:
            first, second = second, first

        # we need to check if they are overlapping
        # case 1: first[1] >= second[0]
        # case 2: first[1] == (second[0] - 1)

        if (first[1] == (second[0] - 1)) or (first[1] > second[0]):
            # they are overlapping
            return (True, (first[0], max(first[1], second[1])))
        else:
            return (False, None)

    def longestValidParentheses(self, s: str) -> int:
        # this stack will contain pairs of ("(", index) where index is the index of the "("
        # character that we pushed into our stack
        stack = []
        sequences = []

        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(('(', i))
            else:
                if len(stack) > 0:
                    open_index = stack.pop()[1]

                    sequences.append((open_index, i))

        while True:
            # now we have in sequence, all the indices of valid parenthesis in order. We just need to merge them until we get
            # a sequence of distinct index ranges.
            previous_sequence = None

            # this will hold our final list of merged ranges
            merged_sequences = []

            for current_sequence in sequences:
                if previous_sequence is None:
                    previous_sequence = current_sequence
                else:
                    # we need to check if we can merge this sequence with the previous one
                    is_overlap, merged_range = self.mergeIfOverlapping(previous_sequence, current_sequence)

                    if is_overlap:
                        # we merged them
                        previous_sequence = merged_range
                    else:
                        # we add the previous sequence as a sequence in our merged list of sequences and move on
                        merged_sequences.append(previous_sequence)
                        previous_sequence = current_sequence

            # we might exit the loop before adding the merged_range we've been working on
            if previous_sequence is not None:
                merged_sequences.append(previous_sequence)

            if merged_sequences != sequences:
                # we did merges so we need to continue the while loop
                sequences = merged_sequences.copy()
            else:
                break

        # now we go over the ranges in merged_sequences and keep track of the longest range
        longest_valid_substring_length = 0

        for (start, end) in merged_sequences:
            current_substring_length = end - start + 1

            longest_valid_substring_length = int(max(longest_valid_substring_length, current_substring_length))

        return longest_valid_substring_length


'''
    Accepted: Same idea as Solution2 concerning using a stack with indices but without using ranges
'''


class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        longest_valid_substring_length = 0

        # the stack will hold the indices of the '(' we encounter
        stack = []

        # the new substring pattern starts at -1, right before the 0
        # we put -1 to get the calculations correct when we do
        # current_index - [index of the beginning of pattern] to get the current
        # length of the substring
        # -1 covers when we have a pattern of valid parentheses starting at 0
        stack.append(-1)

        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    # we need to pop '(' to match our ')'
                    stack.pop()

                if len(stack) == 0:
                    # when the stack empties, this is when we know that we started a new pattern
                    # to get the correct length of the pattern, we always need to do current_index - the
                    # index marking the beginning of the new pattern, to get the right current substring length
                    stack.append(i)
                else:
                    longest_valid_substring_length = int(max(longest_valid_substring_length, i - stack[len(stack) - 1]))

        return longest_valid_substring_length


'''
    Accepted: Dynamic Programming Solution
'''


class Solution4:
    def longestValidParentheses(self, s: str) -> int:
        # this variable will help us keep track of the longest valid substring we find
        longest_substring_length = 0

        # we will use a dp array to save our previously computed work
        # dp[i] will hold the length of the longest valid parentheses substring ending at i
        # since dp will hold indices from 0 to len(s) then its length will be len(s) and by
        # default all the indices will have d[i] 0 since, at the beginning, the length of
        # longest valid substring ending at each index is 0 since we didn't compute anything yet
        dp = [0] * len(s)

        # another observation is that we won't update dp unless we encounter a ')' character
        # since a valid substring can't end with an open parenthesis.

        for i in range(1, len(s)):
            # at each step we will check s[i] and s[i-1]
            # we have 2 cases: )) or () [we won't care about the cases ending with '(']
            if s[i] == ')':
                if s[i - 1] == ')':
                    # ))
                    # we need to check if the ')' at i-1 is part of a valid substring
                    # if it is, then we need to check the character before this valid substring
                    # is a ( because if it is, then this ( we found closes the current )
                    if ((i - dp[i - 1] - 1) >= 0) and s[i - dp[i - 1] - 1] == '(':
                        # dp[i-1] is the length of the substring ending at i-1 so by doing
                        # i - dp[i-1] we are reaching the beginning of the valid substring
                        # then by doing an additional -1, we'd be reaching the character just before it

                        # that means that the valid substring that ends with i is actually
                        # [the valid substring that ends at (i-1)] + [ the ( we went back to find and the
                        # ) we're currently at] + [the valid substring ending at the character just before
                        # the ( that we went back to find => s[i - dp[i-1] - 2] ]
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                        else:
                            dp[i] = dp[i - 1] + 2
                else:
                    # ()
                    # in this case, it means we found a valid set of parenthesis, so the longest
                    # valid substring ending at i will either be () or () + the length of the valid
                    # susbtring ending at s[i-2] (i.e. adjacent to the '()' we just found)
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2

            longest_substring_length = int(max(longest_substring_length, dp[i]))

        return longest_substring_length


# s = "(()"
# s = "()(()"
# s = ")()())"
# s = ""
# s = ")"
# s = "()"
# s = ")(((((()())()()))()(()))("
# s = ")()())()()()"
# s = "()(())"
# s = "()(()()"
# s = "()()"
# s = "("

s = '()(()'

print(Solution3().longestValidParentheses(s))
