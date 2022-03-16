'''
    https://leetcode.com/problems/swap-adjacent-in-lr-string/

    777. Swap Adjacent in LR String

    In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one
    occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and
    the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
'''

'''
    Correct but time limit exceeded
    
    Maybe we can save the results of start and end if we eventually reached a conclusion whether they match or not
'''


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # XL => LX
        # RX => XR

        # base case is if they match
        if start == end:
            return True

        # this will map each index to the string we can substitute it with
        index_to_substitution = {}

        # we will use i to loop over start to find all possible moves
        i = 0

        # we loop over the strings to see what possible moves we can make
        while i < len(start):
            # if we have at least one more character in start then we can
            # test 2 characters together to see if a move exists
            if i + 1 < len(start):
                start_substring = start[i] + start[i + 1]

                if start_substring == "XL":
                    # we have a possible move so we continue to next character
                    index_to_substitution[i] = "LX"
                elif start_substring == "RX":
                    # we have a possible move so we continue to next character
                    index_to_substitution[i] = "XR"

            i += 1

        # now that we found all possible moves, we need to see if one of them eventually leads to a solution
        for index in index_to_substitution:
            substitution = index_to_substitution[index]

            new_start = start[:index] + substitution + start[index + 2:]

            # check if we can reach a solution with the new_start
            is_solution = self.canTransform(new_start, end)

            if is_solution:
                return True

        # if none of the moves returned a solution OR if we don't have any moves to make, then we return False
        return False


'''
    The below solution is better in speed that the one above but maybe we can get rid of the 2 loops and have only one loop?
'''


class Solution2:
    def canTransformHelper(self, start: str, end: str, memo: dict) -> bool:
        # XL => LX
        # RX => XR

        # base case is if they match
        if start == end:
            return True

        if start in memo:
            return memo[start]

        # this will map each index to the string we can substitute it with
        index_to_substitution = {}

        # we will use i to loop over start to find all possible moves
        i = 0

        # we loop over the strings to see what possible moves we can make
        while i < len(start):
            # if we have at least one more character in start then we can
            # test 2 characters together to see if a move exists
            if i + 1 < len(start):
                start_substring = start[i] + start[i + 1]

                if start_substring == "XL":
                    # we have a possible move so we continue to next character
                    index_to_substitution[i] = "LX"
                elif start_substring == "RX":
                    # we have a possible move so we continue to next character
                    index_to_substitution[i] = "XR"

            i += 1

        # now that we found all possible moves, we need to see if one of them eventually leads to a solution
        for index in index_to_substitution:
            substitution = index_to_substitution[index]

            new_start = start[:index] + substitution + start[index + 2:]

            # check if we can reach a solution with the new_start
            is_solution = self.canTransformHelper(new_start, end, memo)

            if is_solution:
                memo[new_start] = True
                memo[start] = True

                return True
            else:
                memo[start] = False
                memo[new_start] = False

        memo[start] = False

        # if none of the moves returned a solution OR if we don't have any moves to make, then we return False
        return False

    def canTransform(self, start: str, end: str) -> bool:
        # will map a version of start to True (if the start version can be transformed into end) and False otherwise
        memo = {}

        return self.canTransformHelper(start, end, memo)


# of where the change was made. So, if we change RXXLRXRXL to XRXLRXRXL, we only pass [..]XLRXRXL to the recursion
class Solution3:
    def canTransformHelper(self, start: str, end: str, memo: dict) -> bool:
        print(start + ' vs ' + end)
        # XL => LX
        # RX => XR

        # base case is if they match
        if start == end:
            return True

        if start in memo:
            return memo[start]

        # we will use i to loop over start to find all possible moves
        i = 0

        # we loop over the strings to see what possible moves we can make
        while i < len(start):
            # if we have at least one more character in start then we can
            # test 2 characters together to see if a move exists
            if i + 1 < len(start):
                start_substring = start[i] + start[i + 1]
                end_substring = end[i] + end[i + 1]

                # we should only do a move if the corresponding substring in end doesn't match the current substring in start
                if start_substring == "XL" or start_substring == "RX" and start_substring != end_substring:
                    # we have a possible move so we continue to` next character
                    substitution = ("XR", "LX")[start_substring == "XL"]

                    new_start = start[:i] + substitution + start[i + 2:]

                    # check if we can reach a solution with the new_start
                    is_solution = self.canTransformHelper(new_start, end, memo)

                    if is_solution:
                        memo[new_start] = True
                        memo[start] = True

                        return True
                    else:
                        memo[start] = False
                        memo[new_start] = False

            i += 1

        memo[start] = False

        # if none of the moves returned a solution OR if we don't have any moves to make, then we return False
        return False

    def canTransform(self, start: str, end: str) -> bool:
        # will map a version of start to True (if the start version can be transformed into end) and False otherwise
        memo = {}

        return self.canTransformHelper(start, end, memo)


'''
    Accepted
'''


class Solution4:
    def canTransform(self, start: str, end: str) -> bool:
        # XL => LX
        # RX => XR

        # we never swap an L with an R so the only thing that changes
        # between start and end is the order of X, so if we remove
        # X from start and end we should have matching strings. If not, then we return false.
        if len(start) != len(end):
            return False

        if start.replace('X', '') != end.replace('X', ''):
            return False

        # the only substitution we have related to L is when we move L to the left
        # so, the indices of L in start should be greater than indices of L in end
        L_start_indices = []
        L_end_indices = []

        # the only substitution we have related to R is when we move R to the right
        # so, the indices of R in start should be less than indices of R in end
        R_start_indices = []
        R_end_indices = []

        for i in range(0, len(start)):
            if start[i] == 'L':
                L_start_indices.append(i)

            if end[i] == 'L':
                L_end_indices.append(i)

            if start[i] == 'R':
                R_start_indices.append(i)

            if end[i] == 'R':
                R_end_indices.append(i)

        for i in range(0, len(L_start_indices)):
            if L_start_indices[i] < L_end_indices[i]:
                return False

        for i in range(0, len(R_start_indices)):
            if R_start_indices[i] > R_end_indices[i]:
                return False

        return True

# print(Solution2().canTransform(start="RXXLRXRXL", end="XRLXXRRLX"))
# print(Solution4().canTransform(start="RXLRXRXL", end="XRXXRRLX"))
# print(Solution4().canTransform("RXXLRXRXL", "XRLXXRRLX"))
# print(Solution2().canTransform(start="XXXXXLXXXX", end="LXXXXXXXXX"))
# print(Solution2().canTransform(start = "X", end = "L"))
# print(Solution2().canTransform("XRXXLXLXXXXRXXXXLXXL", "XXRXLXXLXXRLXXXLXXXX"))
# print(Solution2().canTransform("XXXLXXXXXX", "XXXLXXXXXX"))
# print(Solution3().canTransform("XLXXXXXRXXRXLXXXXXXRXRXXXRXXXLXLLXXLXXXR", "LXRXRXXLXXRXXXRXXXRXLXXXLXXXXXXXXLXXLXRX"))
