'''

    https://leetcode.com/problems/minimum-window-substring/

    76. Minimum Window Substring

    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
    such that every character in t (including duplicates) is included in the window.
    If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.
'''
import math

'''
    Accepted but time limit exceeded
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window_size = float('inf')
        min_window = None

        # i will loop over s
        i = 0

        while i < len(s):
            # we create a copy of t so we don't ruin t for future iterations
            t_copy = t
            start_index = -1
            end_index = -1

            while i < len(s) and t_copy != "":
                if s[i] in t_copy:
                    t_copy = t_copy.replace(s[i], '', 1)

                    if start_index == -1:
                        start_index = i

                    end_index = i

                i += 1

            # either i >= len(s) or we found all the characters in t
            if t_copy != "":
                # the remaining substring of s does not contain all the characters in t
                break
            else:
                # check current window size
                current_window_size = end_index - start_index + 1

                if current_window_size < min_window_size:
                    min_window_size = current_window_size
                    min_window = (start_index, end_index)

            # we are done with finding a complete window, now we need to look
            # for another one (possibly smaller) then begins after start_index
            i = start_index + 1

        if min_window is None:
            return ""
        else:
            return s[min_window[0]:min_window[1] + 1]


'''
    Let's try a greedy approach where we always choose the smallest window?
'''


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
        elif t in s:
            return t

        # if we reach here we know that t has more than one character
        # also we know that t is not a substring of s

        char_to_indices = {}

        # we create a key for every character in t
        for char in t:
            char_to_indices[char] = []

        # we fill char_to_index st each character in t is mapped
        # to indices in s
        for i in range(0, len(s)):
            if s[i] in char_to_indices:
                char_to_indices[s[i]].append(i)

        # now we loop over every pair of indices and try to incrementally
        # add to our list of characters but by always choosing the index that would
        # minimize our window
        window_start = -1
        window_end = -1
        indices = set()

        # since we're sure that t has more than 1 character, we can safely start our computations
        # on t[0] and t[1]
        first_indices = char_to_indices[t[0]]
        second_indices = char_to_indices[t[1]]
        min_window_size = float('inf')

        # we need to greedily choose out of first_indices and second_indices
        # the pair with least difference
        for i in first_indices:
            for j in second_indices:
                if i != j:
                    # do this because we could have duplicate characters which will map
                    # to same indices => in such cases we need to choose different indices for the same char
                    current_window_size = max(i, j) - min(i, j) + 1

                    if current_window_size < min_window_size:
                        min_window_size = current_window_size
                        window_start = min(i, j)
                        window_end = max(i, j)

        # after we are done here, we should have a min_window_size
        if math.isinf(min_window_size):
            # couldn't find a suitable window (happens when we have for example aa in t and only one a in s)
            return ""
        else:
            # we were able to find a suitable window
            indices.add(window_start)
            indices.add(window_end)

            # now we continue going through the remaining characters in t
            for i in range(2, len(t)):
                current_indices = char_to_indices[t[i]]
                current_min_window = float('inf')
                current_min_window_index = -1

                # we need to choose the index that minimizes the window size
                for index in current_indices:
                    if index not in indices:
                        # to take care of duplicate characters, we make sure that
                        # we don't repeat indices in our window
                        if index < window_end and index > window_start:
                            # we can safely choose this index because it won't make
                            # the current window we chose greater
                            current_min_window_index = index
                            # we break because we found a good index for the current character in t
                            break
                        elif index > window_end:
                            # we need to compare it with window_start
                            if current_min_window > (index - window_start + 1):
                                current_min_window = (index - window_start + 1)
                                current_min_window_index = index
                        elif index < window_start:
                            # we need to compare it with window_end
                            if current_min_window > (window_end - index + 1):
                                current_min_window = (window_end - index + 1)
                                current_min_window_index = index

                if current_min_window_index != -1:
                    # we found a suitable index for the current character
                    indices.add(current_min_window_index)

                    # we change our window based on the index we just added
                    window_start = min(window_start, current_min_window_index)
                    window_end = max(window_end, current_min_window_index)
                else:
                    # we couldn't find a suitable index for the current character in t
                    # which means that we don't have a solution for this case
                    return ""

            if window_start != -1 and window_end != -1:
                return s[window_start: window_end + 1]
            else:
                return ""


'''
    Accepted: In the below solution, we keep track of needed_letters_counts (i.e. the number of letters still needed
    in the current window of s to have all the letters in t). Then we use 2 points start and end to go through a list
    called sequence. Sequence is only a list of tuples (index, char) that shows the index and character of every letter
    in s that is in t (i.e. helps us get rid of all the other letters that we don't care about). Then we move start and end
    1 index at a time and each time we check if the window is valid (has all the letters), if it is we note its window width.
    Note that since we're moving the start and end pointers one by one, we can incrementally update the needed_letters_counts
    without having to recompute it for every window.
    
    Runtime: O(m+n)
'''


class Solution3:
    def isValidWindow(self, counts):
        for key in counts:
            if counts[key] > 0:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        # first we transform t into a dict count
        needed_letter_counts = {}

        # O(m)
        for char in t:
            if char in needed_letter_counts:
                needed_letter_counts[char] += 1
            else:
                needed_letter_counts[char] = 1

        sequence = []

        # O(n)
        for i in range(0, len(s)):
            if s[i] in t:
                sequence.append((i, s[i]))

        # now we loop over sequence
        # we keep looping until we find a window that has all characters in t
        # once we find such a window, we calculate its size and move on to another
        start = 0
        end = start - 1

        # indices of the start and end of elements in sequence that mark the window
        # that contains all the letters in t
        min_window = None
        min_window_size = float('inf')

        # O(n) => since sequence is a subset of the letters in s so worst-case it's O(n)
        while start < len(sequence):
            while end < (len(sequence) - 1) and not self.isValidWindow(needed_letter_counts):
                end += 1

                # starting at `start` let's keep increasing `end` until we find all the letters in t
                index, char = sequence[end]

                # we decrease the counts of character because we found one match
                needed_letter_counts[char] -= 1

            # when we reach this point it's either because end >= len(sequence)
            # OR we found a valid window from sequence[start] to sequence[end]
            if self.isValidWindow(needed_letter_counts):
                # it means that we need to check the size of this window to see if it's minimum
                current_window_size = sequence[end][0] - sequence[start][0] + 1

                if current_window_size < min_window_size:
                    min_window_size = current_window_size
                    min_window = (start, end)

                # now we need to move on to the next window
                # first we need to update the count of the character that's at sequence[start]
                needed_letter_counts[sequence[start][1]] += 1  # because it's no longer in our current window
                start += 1
            else:
                # window is not valid and end surpassed sequence
                # we no longer have solutions
                break

        if min_window is not None:
            return s[sequence[min_window[0]][0]:sequence[min_window[1]][0] + 1]
        else:
            return ""


# s = "ADOBECODEBANC"
# t = "ABBC"

# s = "a"
# t = "a"

# s = "a"
# t = "aa"

# s = "bba"
# t = "ab"

print(Solution3().minWindow(s, t))
