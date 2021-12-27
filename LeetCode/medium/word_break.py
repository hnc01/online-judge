'''
    https://leetcode.com/problems/word-break/

    139. Word Break

    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

'''
    Without saving results, we get Time Limit Exceeded
    By saving results, we get Accepted
    
    Without saving the results, the runtime of brute force is O(2^n)
    By saving the results, the runtime can be cut-down to O(n^3)
'''


class Solution:
    def word_break_helper(self, s, wordDict, memo):
        if not s:
            # s is empty it means we found all the pieces of s that are in wordDict and we're not left
            # with any pieces so the different sections can be found in wordDict
            return True
        elif s in memo:
            return memo[s]
        else:
            # we try to split in different positions
            for i in range(0, len(s)):
                left_word = s[0:i + 1]

                if left_word in wordDict:
                    is_valid = self.word_break_helper(s[i + 1:], wordDict, memo)

                    if is_valid:
                        memo[s] = True
                        return True

            memo[s] = False

            return False

    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        memo = {}
        wordDict = set(wordDict)

        return self.word_break_helper(s, wordDict, memo)


'''
    Dynamic Programming solution relies on making sure that we have results of smaller sizes computed
    before we proceed with bigger sizes. It's same approach as above except that by ordering the sizes
    we explore, we can solve the problem without recursive calls
    
    Also Accepted
'''


class Solution2:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        # we need to save memory of all string sizes so the keys should go from
        # size 0 to size len(s) (included, so we add 1)
        memo = [False] * (len(s) + 1)
        wordDict = set(wordDict)  # we always turn this into a set so that the `in` operation is fast O(1)

        # we know that if a string is of size 0, then automatically we return True (just like base case in above where s is empty)
        memo[0] = True

        # We also use two index pointers ii and jj, where ii refers to the length of the substring (s')
        # considered currently starting from the beginning, and jj refers to the index partitioning the current substring (s')
        # into smaller substrings s'(0,j) and s'(j+1,i).

        # now we loop over all possible substring where we make a cut in the string at i
        for i in range(1, len(s) + 1):
            # j will be all possible decompositions of size i
            for j in range(0, i):
                # the substring [j,i] is the one we're currently inspecting
                # check if the substring from 0 to j is True and if the substring between j and i is in word dict
                if memo[j] and s[j:i] in wordDict:
                    # the current cut at i works
                    # Note: after debug, what memo[i] means is that the substring [0, i] has a decomposition where all parts are in wordDict
                    memo[i] = True
                    # we found one case where the cut at i works so no need to proceed
                    break

        # finally we return the result of decomposition over the entire string
        return memo[len(s)]


# s = "leetcode"
# wordDict = ["leet","code"]

s = "applepenapple"
wordDict = ["apple", "pen"]

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

print(Solution2().wordBreak(s, wordDict))
