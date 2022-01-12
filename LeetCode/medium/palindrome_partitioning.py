'''
    https://leetcode.com/problems/palindrome-partitioning/

    131. Palindrome Partitioning

    Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

    A palindrome string is a string that reads the same backward as forward.

    Check the following video for thorough explanation: https://www.youtube.com/watch?v=3jvWodd7ht0
'''

'''
    Brute Force Backtracking
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

    def dfs(self, start_index, current_list, s, results):
        if start_index >= len(s):
            # we reached the end of our string and current_list satisfies our conditions (otherwise we wouldn't have reached here)
            # so we append current_list to results
            results.append(current_list)
        else:
            # we need to generate all possible substrings we can get from s start at start_index
            # what this loop does is partition a string incrementally starting at a certain index [our substring]
            # c[aab] => c[a|ab] => recursively handle ca[ab] => [ab] fail because not palindrome BUT [a|b] works because each palindrome => c[a,a,b]
            # c[aab] => c[aa|b] => recursively handle caa[b] => [b] is one string so palindrome => c[aa,b]
            # c[aab] => c[aab] => won't work because aab is not palindrome
            for end_index in range(start_index, len(s)):
                # first end_index = start_index => we're checking only one character substrings s[start_index]
                if self.is_palindrome(s, start_index, end_index):
                    current_list_copy = current_list.copy()

                    # the current substring is a palindrome so we need to add it to our current list
                    current_list_copy.append(s[start_index:end_index + 1])

                    # now we explore the remaining part of the string to see if this current branch can lead to any results
                    self.dfs(end_index + 1, current_list_copy, s, results)

                    # since we add our current substring to a copy of current_list, we when we iterate in the loop again with another end_index
                    # the last substring we added won't be there because it was added to a copy of current_list and not current_list itself

    def partition(self, s: str) -> [[str]]:
        # this will hold our final result: list of lists of palindrome substrings
        results = []

        self.dfs(0, [], s, results)

        return results


'''
    Backtracking + DP
    
    The above can be optimize by reducing computations of isPalindrome(). If we know that s[start + 1 ... end - 1] is a palindrome, then for sure the substring
    s[start ... end] is a palindrome IF s[start] = s[end]. So, we don't need reiterate over the characters from start to end, we can get our answer from our dp array
'''


class Solution2:
    def dfs(self, start_index, current_list, s, results, dp):
        if start_index >= len(s):
            # we reached the end of our string and current_list satisfies our conditions (otherwise we wouldn't have reached here)
            # so we append current_list to results
            results.append(current_list)
        else:
            # we need to generate all possible substrings we can get from s start at start_index
            # what this loop does is partition a string incrementally starting at a certain index [our substring]
            # c[aab] => c[a|ab] => recursively handle ca[ab] => [ab] fail because not palindrome BUT [a|b] works because each palindrome => c[a,a,b]
            # c[aab] => c[aa|b] => recursively handle caa[b] => [b] is one string so palindrome => c[aa,b]
            # c[aab] => c[aab] => won't work because aab is not palindrome
            for end_index in range(start_index, len(s)):
                # first end_index = start_index => we're checking only one character substrings s[start_index]

                # the palindrome check has 2 clauses:
                # s[start_index] == s[end_index] => making sure that the first and last characters of the current substring match
                # (end_index - start_index <= 2 or dp[start_index + 1][end_index - 1]) has 2 clauses:
                #   end_index - start_index <= 2 => by default any string of length 1 or 0 is a palindrome. By reaching here we know that
                #   s[start_index] == s[end_index] so if the length of the string 2 (e.g., 'aa', 'bb') or 3 (e.g., 'aba', 'bbb'),
                #   for sure it's also a palindrome.
                #
                #   dp[start_index + 1][end_index - 1] => we reached here knowing that s[start_index] == s[end_index] AND length of substring
                #   is more than 2 => we check if the inner substring is a palindrome by consulting with array
                if s[start_index] == s[end_index] and (end_index - start_index <= 2 or dp[start_index + 1][end_index - 1]):
                    dp[start_index][end_index] = True

                    current_list_copy = current_list.copy()

                    # the current substring is a palindrome so we need to add it to our current list
                    current_list_copy.append(s[start_index:end_index + 1])

                    # now we explore the remaining part of the string to see if this current branch can lead to any results
                    self.dfs(end_index + 1, current_list_copy, s, results, dp)

                    # since we add our current substring to a copy of current_list, we when we iterate in the loop again with another end_index
                    # the last substring we added won't be there because it was added to a copy of current_list and not current_list itself

    def partition(self, s: str) -> [[str]]:
        # this will hold our final result: list of lists of palindrome substrings
        results = []

        dp = [[]] * len(s)

        for i in range(0, len(s)):
            dp[i] = [False] * len(s)

        # all substrings of length 1 are by default palindromes
        for i in range(0, len(s)):
            dp[i][i] = True

        self.dfs(0, [], s, results, dp)

        return results


# s = 'aabbcecbbdd'
# s = 'abcceccb'
# s = 'aab'
s = "bbab"
print(Solution2().partition(s))
