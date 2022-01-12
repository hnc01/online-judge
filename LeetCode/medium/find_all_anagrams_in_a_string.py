'''
    https://leetcode.com/problems/find-all-anagrams-in-a-string/

    438. Find All Anagrams in a String

    Given two strings s and p, return an array of all the start indices of p's anagrams in s.
    You may return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
'''

'''
    Correct but Time Limit Exceeded
'''


class Solution:
    def is_anagram(self, substring, p_counts):
        substring_counts = {}

        for character in substring:
            if character not in substring_counts:
                substring_counts[character] = 0

            substring_counts[character] += 1

        # now we need to check if the counts of each character in substring match the count in p
        for character in substring_counts:
            if character not in p_counts:
                return False
            elif character in p_counts and p_counts[character] != substring_counts[character]:
                return False

        return True

    def findAnagrams(self, s: str, p: str) -> [int]:
        # map each character in p to its count
        p_counts = {}

        for character in p:
            if character not in p_counts:
                p_counts[character] = 0

            p_counts[character] += 1

        results = []

        for i in range(0, len(s)):
            if i + len(p) <= len(s):
                # s[i: i + len(p)] = s[i .. len(p) - 1]
                current_substring = s[i: i + len(p)]

                if self.is_anagram(current_substring, p_counts):
                    results.append(i)

        return results


'''
    The bottleneck of the above solution is that we have to iterate over the entire substring to see if it's an anagram
    Maybe instead of re-iterating from scratch everytime, we can incrementally maintain a count of the characters in the
    current substring we're examining.
'''

'''
    Accepted
'''


class Solution2:
    def is_anagram(self, substring_counts, p_counts):
        # now we need to check if the counts of each character in substring match the count in p
        for character in substring_counts:
            if substring_counts[character] > 0 and character not in p_counts:
                return False
            elif character in p_counts and p_counts[character] != substring_counts[character]:
                return False

        return True

    def findAnagrams(self, s: str, p: str) -> [int]:
        # there aren't enough characters in s to attempt to generate p
        if len(p) > len(s):
            return []

        # moving forward here, we know that we have at least as many characters in s as we do in p

        # map each character in p to its count
        p_counts = {}

        for character in p:
            if character not in p_counts:
                p_counts[character] = 0

            p_counts[character] += 1

        substring_counts = {}

        # first we need to add the first len(p) characters in s to the count (because in the iteration, we will always remove
        # the left-most character from the counts and adding a new character to the counts)
        for i in range(0, len(p)):
            character = s[i]

            if character not in substring_counts:
                substring_counts[character] = 0

            substring_counts[character] += 1

        results = []

        if self.is_anagram(substring_counts, p_counts):
            results.append(0)

        i = 1  # with each iteration, this will move one to the right
        j = len(p)  # with each iteration, this will move one to the right

        # we will test for j only because it will reach the end first
        while j < len(s):
            old_character = s[i - 1]
            new_character = s[j]

            # we need to remove old_character from our substrings_count
            substring_counts[old_character] -= 1

            # we need to add the new_character to our substrings_count
            if new_character not in substring_counts:
                substring_counts[new_character] = 0

            substring_counts[new_character] += 1

            # test if the new substring is an anagram
            if self.is_anagram(substring_counts, p_counts):
                # the current substring starts at i
                results.append(i)

            i += 1
            j += 1

        return results


s = "cbaebabacd"
p = "abc"

# s = "abab"
# p = "ab"

print(Solution2().findAnagrams(s, p))
