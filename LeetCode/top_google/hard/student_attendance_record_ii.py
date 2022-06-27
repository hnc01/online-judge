'''
    https://leetcode.com/problems/student-attendance-record-ii/

    552. Student Attendance Record II

    An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or
    present on that day. The record only contains the following three characters:
    - 'A': Absent.
    - 'L': Late.
    - 'P': Present.

    Any student is eligible for an attendance award if they meet both of the following criteria:
    - The student was absent ('A') for strictly fewer than 2 days total.
    - The student was never late ('L') for 3 or more consecutive days.

    Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award.

    The answer may be very large, so return it modulo 10^9 + 7.
'''

'''
    TLE
'''


class Solution:
    def generateRecords(self, n, nbOfA, nbOfConsecutiveL):
        if n == 0:
            # we filled all the days successfully for this branch
            return 1
        else:
            # we still have days to fill
            # the current day can be a:
            # - P
            # - L if the last 2 characters were not L
            # - A if nbOfA < 1

            # choosing P for current letter
            choosingP = self.generateRecords(n - 1, nbOfA, 0)

            # choosing L for current letter
            if nbOfConsecutiveL <= 1:
                choosingL = self.generateRecords(n - 1, nbOfA, nbOfConsecutiveL + 1)
            else:
                choosingL = 0

            # choosing A for current letter
            if nbOfA < 1:
                choosingA = self.generateRecords(n - 1, nbOfA + 1, 0)
            else:
                choosingA = 0

            # we need to do mod for every result to make sure we don't have an overflow at any stage of our addition
            return (choosingP % ((10 ** 9) + 7)) + (choosingL % ((10 ** 9) + 7)) + (choosingA % ((10 ** 9) + 7))

    def checkRecord(self, n: int) -> int:
        return self.generateRecords(n, 0, 0) % ((10 ** 9) + 7)


'''
    Same as the above solution but with memoization.
    
    It goes too deep in recursion so it still isn't a valid solution because it's stack overflow.
    
    So, DP top down with memoization isn't a good performance. We need a bottom up iterative solution.
'''


class Solution2:
    def generateRecords(self, n, nbOfA, nbOfConsecutiveL, memo):
        if n == 0:
            # we filled all the days successfully for this branch
            return 1
        else:
            # we still have days to fill
            # the current day can be a:
            # - P
            # - L if the last 2 characters were not L
            # - A if nbOfA < 1

            if (n, nbOfA, nbOfConsecutiveL) in memo:
                return memo[(n, nbOfA, nbOfConsecutiveL)]

            # choosing P for current letter
            choosingP = self.generateRecords(n - 1, nbOfA, 0, memo)

            # choosing L for current letter
            if nbOfConsecutiveL <= 1:
                choosingL = self.generateRecords(n - 1, nbOfA, nbOfConsecutiveL + 1, memo)
            else:
                choosingL = 0

            # choosing A for current letter
            if nbOfA < 1:
                choosingA = self.generateRecords(n - 1, nbOfA + 1, 0, memo)
            else:
                choosingA = 0

            # we need to do mod for every result to make sure we don't have an overflow at any stage of our addition
            result = (choosingP % ((10 ** 9) + 7)) + (choosingL % ((10 ** 9) + 7)) + (choosingA % ((10 ** 9) + 7))

            memo[(n, nbOfA, nbOfConsecutiveL)] = result

            return result

    def checkRecord(self, n: int) -> int:
        memo = {}

        return self.generateRecords(n, 0, 0, memo) % ((10 ** 9) + 7)


'''
    - We know that our cache/dp/memo should be of the form (n, nbOfA, nbOfConsecutiveL)
    - We know that a string is of the form [n - 1 character] [nth character] and with each iteration we know that all the solutions
      we have of all strings of size [n-1] will be the number of acceptable records.
    - So, when we add on our nth character, this is when we need to build on our previous solutions of size [n-1] to get the number
      of acceptable representations for strings of size [n].
    - If the nth character we're adding is P, then we don't need to care of any special cases because adding a P to an [n-1] acceptable 
      string would still lead to acceptable string.
    - If the nth character we're adding is an A, then we need to make sure that our [n-1] strings are all with nbOfA = 0.
    - If the nth character we're adding is an L, then we need to make sure that our [n-1] strings are all with nbOfConsecutiveL <= 1.
    - We also need to base cases which we'll take when n = 1. 
'''

'''
    Accepted
'''


class Solution3:
    def checkRecord(self, n: int) -> int:
        MOD = (10 ** 9) + 7

        '''
            Note: we're perform % at each point of summations to make sure we don't overflow at any point
        '''

        dp = {}

        # the indices of dp are of the form (n, nbOfA, nbOfConsecutiveL)
        # the acceptable values of nbOfA are 0 and 1.
        # the acceptable values of nbOfConsecutiveL are 0, 1 and 2.
        # our bases cases are: (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2)
        dp[(1, 0, 0)] = 1  # no A and no L and length 1 => P
        dp[(1, 0, 1)] = 1  # no A and 1 L and length 1 => L
        dp[(1, 0, 2)] = 0  # no A and 2 L and length 1 => impossible
        dp[(1, 1, 0)] = 1  # 1 A  and no L and length 1 => A
        dp[(1, 1, 1)] = 0  # 1 A  and 1 L and length 1 => impossible
        dp[(1, 1, 2)] = 0  # 1 A  and 2 L and length 1 => impossible

        # now that we are done with our base cases, we need to move from length 2 up to strings with length n
        for i in range(2, n + 1):
            # we need to fill at each step the below values

            # we will end up with 0 A and 0 consecutive L at the end
            # the only we can reach state (i, 0, 0) is if we have an [n-1] string and we're appending a P to it
            # because we have 0 A and no Ls at the end
            # we can reach here by coming from a state that has 0 A and [ends with P and we're appending another P
            # OR ends with L and we're a P OR ends with LL and we're appending a P]
            # these states translate to (i-1, 0, 0) OR (i-1, 0, 1) OR (i-1, 0, 2)
            dp[(i, 0, 0)] = (dp[(i - 1, 0, 0)] + dp[(i - 1, 0, 1)] + dp[(i - 1, 0, 2)]) % MOD

            # we will end up with 0 A and 1 L at the end: ...[L]
            # to get here we need to come from a state with 0 A and 0 L
            dp[(i, 0, 1)] = dp[(i - 1, 0, 0)] % MOD

            # we will end up now with 2 Ls at the end and no A: ....L[L]
            # to reach this state, we need to come from a state that has 0 A and 1 L at the end
            dp[(i, 0, 2)] = dp[(i - 1, 0, 1)] % MOD

            # we will end up now with a string that has 1 A and ends with 0 consecutive L
            # to reach a state like this, we can come from:
            # - state with 0 A and we're appending the A now (so all states (i, 0, x)
            # - state with 1 A already and we're appending a P now to get 0 consecutive L => can come from 0 L, 1 L or 2 L
            dp[(i, 1, 0)] = (((dp[(i - 1, 0, 0)] + dp[(i - 1, 0, 1)] + dp[(i - 1, 0, 2)]) % MOD) + ((dp[(i - 1, 1, 0)] + dp[(i - 1, 1, 1)] + dp[(i - 1, 1, 2)]) % MOD)) % MOD

            # we will end up now with 1 L at the end of string and 1 A: ..A..[L]
            # to reach this state, we need to come from a state with 1 A and no L at the end
            dp[(i, 1, 1)] = dp[(i - 1, 1, 0)] % MOD

            # we will end up now with 2 consecutive Ls in the string and 1 A: ..A..L[L]
            # we consider L consecutive only if they're at the end of the string (because other Ls in previous
            # part of string are already taken care of
            # to reach this state, we need to come from a state where we had 1 A and 1 L (at the end)
            dp[(i, 1, 2)] = dp[(i - 1, 1, 1)] % MOD

        return (((dp[(n, 0, 0)] + dp[(n, 0, 1)] + dp[(n, 0, 2)]) % MOD) + ((dp[(n, 1, 0)] + dp[(n, 1, 1)] + dp[(n, 1, 2)]) % MOD)) % MOD


print(Solution3().checkRecord(2))
print(Solution3().checkRecord(1))
print(Solution3().checkRecord(10101))
