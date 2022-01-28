'''
    https://leetcode.com/problems/edit-distance/

    72. Edit Distance

    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

    You have the following three operations permitted on a word:

    - Insert a character
    - Delete a character
    - Replace a character
'''

'''
    Accepted but time limit exceeded.
    
    When we replace, insert, or delete we might end up with word1 and word2 substrings that we've seen before.
    Try a DP solution.
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # we always consider word1[0] and word2[0] as the characters we're dealing with
        if len(word1) == 0:
            # to obtain word2 we need to add len(word2) characters to word1 to obtain word2
            return len(word2)
        elif len(word2) == 0:
            # to obtain word2 we need to delete len(word1) characters from word1
            return len(word1)
        else:
            # len(word1) > 0 and len(word2) > 0
            # at each character we have 4 options:
            # 1) if word1[0] == word2[0] => do nothing => minDistance(word1[1:], word2[1:])
            # 1) if word1[0] != word2[0] => delete word1[0] => 1 + minDistance(word1[1:], word2)
            # 2) if word1[0] != word2[0] => add char to word1 => 1 + minDistance(word1, word2[1:])
            # 3) if word1[0] != word2[0] => replace word1[0] with word2[0] => 1 + minDistance(word1[1:], word2[1:])
            if word1[0] == word2[0]:
                # do nothing proceed to next characters
                # dp[i][j] = dp[i+1][j+1]
                return self.minDistance(word1[1:], word2[1:])
            else:
                # dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                delete_operations_count = 1 + self.minDistance(word1[1:], word2)
                insert_operations_count = 1 + self.minDistance(word1, word2[1:])
                replace_operations_count = 1 + self.minDistance(word1[1:], word2[1:])

                return min(delete_operations_count, insert_operations_count, replace_operations_count)


'''
    Do the same as above but with indices instead of trimming the string.
    The below is accepted. Just need to turn it into dp solution.
'''


class Solution2:
    def minDistanceHelper(self, word1, word2, i, j) -> int:
        # we always consider word1[0] and word2[0] as the characters we're dealing with
        if i >= len(word1):
            # to obtain word2 we need to add what's left of word2 to word1
            return len(word2) - j
        elif j >= len(word2):
            # to obtain word2 we need to delete what's left of word1
            return len(word1) - i
        else:
            # we still have characters in both words
            # at each character we have 4 options:
            # 1) if word1[i] == word2[j] => do nothing => minDistance(word1, word2, i+1, j+1)
            # 1) if word1[i] != word2[j] => delete word1[i] => 1 + minDistance(word1, word2, i+1, j)
            # 2) if word1[i] != word2[j] => add char to word1 => 1 + minDistance(word1, word2, i, j+1)
            # 3) if word1[i] != word2[j] => replace word1[i] with word2[j] => 1 + minDistance(word1, word2, i+1, j+1)
            if word1[i] == word2[j]:
                # do nothing proceed to next characters
                # dp[i][j] = dp[i+1][j+1]
                return self.minDistanceHelper(word1, word2, i + 1, j + 1)
            else:
                # dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                delete_operations_count = self.minDistanceHelper(word1, word2, i + 1, j)
                insert_operations_count = self.minDistanceHelper(word1, word2, i, j + 1)
                replace_operations_count = self.minDistanceHelper(word1, word2, i + 1, j + 1)

                return 1 + min(delete_operations_count, insert_operations_count, replace_operations_count)

    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceHelper(word1, word2, 0, 0)


'''
    Accepted: DP solution (bottom up)
'''


class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        # since in Solution2 we're always changing 2 indices, i and j, we need
        # our dp array to be 2D. The first dimension will index word1 (i) and
        # the second dimension will index word2 (j).
        # However, we notice that in the above solution, we have base where
        # i >= len(word1) and j >= len(word2). Which means, that the solutions of
        # these bases needs to be in dp. So, the i dimension will include len(word1)
        # as an index and the j dimension will include len(word2) as an index
        dp = [[]] * (len(word1) + 1)

        for i in range(0, len(word1) + 1):
            dp[i] = [float('inf')] * (len(word2) + 1)

        # from the above base cases, we know that dp[len(word1)][j] = len(word2) - j
        for j in range(0, len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # from the above base cases, we know that dp[i][len(word2)] = len(word1) - i
        for i in range(0, len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        # now that we have our base cases, we notice that in our recursive calls, we always
        # refer to i, j, i+1 or j+1. This means that we need our i+1, j+1 cases to be solved
        # in order to compute dp[i][j]. This means that we need to go through word1 and word2
        # in reverse order.
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

        return dp[0][0]


# word1 = "horse"
# word2 = "ros"

# word1 = "intention"
# word2 = "execution"

word1 = "dinitrophenylhydrazine"
word2 = "acetylphenylhydrazine"

print(Solution3().minDistance(word1, word2))
