'''
    Solution 1: Brute Force
    Gives Time Limit Exceeded
'''


class Solution1:
    def isPalindrome(self, s, start, end):
        j = end

        for i in range(start, int((end + start) / 2) + 1):
            if s[i] != s[j]:
                return False

            j -= 1

        return True

    def longestPalindrome(self, s: str) -> str:
        # let's check all substrings of certain size and see if we can find palindromes
        longest_palindrome = ""

        for current_size in range(1, len(s) + 1):
            # current_size will go from [1 to n] all are different sizes of substrings of s
            # i will go from start of string to end of it and will mark the beginning of a palindrome substring
            for i in range(0, len(s)):
                # the end of this substring will be at i + current_size - 1
                j = i + current_size - 1

                # first we check if j is less than len(s), otherwise the length of this substring exceeds the end of the array
                if j < len(s):
                    # now we need to check if the current substring is a palindrome
                    if self.isPalindrome(s, i, j):
                        # since we break when we find a palindrome of a certain size and immediately go to the second substring size
                        # when we encounter a palindrome, for sure its length is more than the one before it
                        # the string splice [i:j] will exclude the character at j so I do j+1
                        longest_palindrome = s[i:j + 1]

                        break

        return longest_palindrome


'''
    Dynamic Programming Idea [Accepted]: if we have a substring [i,j] and we already know that the substring [i+1, j-1] is a palindrome
    then we don't need to test the whole [i,j] substring. We just test s[i] == s[j] because we already know the answer for [i+1, j-1]
'''


class Solution2:
    substring_palindrome_map = None
    longest_palindrome = ""

    def longestPalindrome(self, s: str) -> str:
        # formulate the problem as subproblems
        # P(i,j) is palindrome if Si == Sj (i.e., first and last characters are equal) AND if substring Si+1 to Sj-1 is a palindrome
        # P(i,j) = (Si == Sj) AND P(i+1, j-1)

        # we first create the nxn matrix where n is length of s
        self.substring_palindrome_map = []

        for i in range(0, len(s)):
            self.substring_palindrome_map.append([None] * len(s))

        # now we need to iterate through the string and first solve the smallest subproblems and work our way up
        # since our subproblem is of the form i+1 it means that we need to make sure we solved the i+1 case before the i
        # so we need to go through the i index in decreasing order
        for i in range(len(s) - 1, -1, -1):
            # now we will examine all substrings starting at i
            # since our subproblem is of the form j-1 then we need to solve subproblems at j in increasing order which is
            # inline with this loop
            for j in range(i, len(s)):
                # this will examine all substrings starting at i and ending at j
                # Note we don't need to examine if we already know the answer to the subproblems
                # because the way we're iterating over the string guarantees that we do
                if i == j:
                    # we have one character so by default we have a palindrome
                    solution = True
                elif j == i + 1:
                    # we have 2 characters so we need to check if they're equal
                    solution = s[i] == s[j]
                else:
                    solution = (s[i] == s[j]) and self.substring_palindrome_map[i+1][j-1]

                self.substring_palindrome_map[i][j] = solution

                if solution and len(self.longest_palindrome) < (j - i + 1):
                    self.longest_palindrome = s[i:j + 1]

        return self.longest_palindrome

print(Solution2().longestPalindrome("aaaaa"))
