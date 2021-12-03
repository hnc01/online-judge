'''
    Given a string s, find the length of the longest substring without repeating characters.
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

'''
    Time Limited Exceeded but this is the accepted brute force approach
'''


class Solution:
    def is_unique_substring(self, s, i, j):
        char_set = set()

        # we do j+1 because we want to include j
        for i in range(i, j + 1):
            if s[i] not in char_set:
                char_set.add(s[i])
            else:
                return False

        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                is_current_substring_unique = self.is_unique_substring(s, i, j)

                if is_current_substring_unique:
                    # we compare the length of this substring with the longest length we found so far
                    longest_substring = max(longest_substring, (j - i + 1))

        return longest_substring


'''
    The second approach is called sliding window basically we have a start index at each iteration and
    we keep adding more characters until we hit a duplicate, when that happens we know that is the longest
    substring at that index, so we save that result and move on (i.e. we don't check all possible substrings
    that can be generated from this position - this helps us eliminate checking unecessary substrings)
'''

'''
    Sliding Window:
    This technique shows how a nested for loop in some problems can be converted to a single for loop to reduce the time complexity.
'''


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we need to keep track of the characters we're already seen
        # we can't use a set like I wanted initially because sometimes we have a situation like 'pwwe'
        # in this case the set would have {p, w}. When we advance the left pointer by one and right pointer by one
        # we'd get wwe however the set shows only one w even though we need to eliminate the other w
        # the only way to correctly keep track of duplicates is if we accurately keep track of their counts
        current_substring_chars = {}

        # we will do the sliding window technique which means that we need 2 pointers:
        # left (left side of the window) and right (right side of the window)
        # everything between left and right will be our current substring
        left = right = 0

        # we also need to keep track of the length of the longest substring we've seen so far
        longest_length = 0

        # we need to keep moving the right pointer from left until the end of the string
        while right < len(s):
            # at the beginning of the loop we have s[right] is a new character
            new_character = s[right]

            if new_character not in current_substring_chars:
                current_substring_chars[new_character] = 0

            # we encountered a character in the string and we need to increase its count
            current_substring_chars[new_character] += 1

            # now we need to make sure that the count of characters in the substring is max 1
            while current_substring_chars[new_character] > 1:
                # if it is then we need to advance the left side of the window to skip the first character in it (this is how the window advances)
                old_character = s[left]

                current_substring_chars[old_character] -= 1

                left += 1

            # now we have a new substring so we need to check its length (remember that current substring is inside the window [left right])
            longest_length = max(longest_length, right - left + 1)

            right += 1

        return longest_length

print(Solution2().lengthOfLongestSubstring("pwwkew"))
