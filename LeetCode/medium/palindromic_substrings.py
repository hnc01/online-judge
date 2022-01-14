'''
    https://leetcode.com/problems/palindromic-substrings/

    647. Palindromic Substrings

    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.
'''

'''
    Accepted but time limit exceeded. Usually, in palindrome problems, we can always make use of the fact that if s[i] == s[j] 
    and s[i+1 .. j-1] is a palindrome, then for sure s[i..j] is a palindrome. So we don't need to recompute anything. 
'''


class Solution:
    # returns True if s[i] .. s[j] is a palindrome
    def is_palindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def countSubstrings(self, s: str) -> int:
        count = 0

        # first let's generate all possible substrings
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if i == j:
                    # we have one character in our substring
                    # no need to make a function call here because this is trivially true
                    count += 1
                elif self.is_palindrome(s, i, j):
                    count += 1

        return count


'''
    Accepted
'''


class Solution2:
    def countSubstrings(self, s: str) -> int:
        count = 0

        dp = [[]] * len(s)

        for i in range(0, len(s)):
            dp[i] = [False] * len(s)

        # since in our solution we rely on the fact that we solved s[i+1..j-1] before s[i..j] then we need to make sure
        # that we're solving i+1 before i so we need go through the array in reverse order and start building our dp
        # of palindrome status with smaller substrings until we reach the beginning of the array.
        for start_index in range(len(s) - 1, -1, -1):
            for end_index in range(start_index, len(s)):
                # we will keep examining strings from start_index to end_index
                # we start at the end of the string
                if s[start_index] == s[end_index] and ((end_index - start_index <= 2) or dp[start_index + 1][end_index - 1]):
                    dp[start_index][end_index] = True

                    count += 1

        return count


# s = 'abc'
# s = 'aaa'
s = "aaaaa"
# s = 'abcd'

print(Solution2().countSubstrings(s))
