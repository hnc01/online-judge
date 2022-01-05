'''
    https://leetcode.com/problems/perfect-squares/

    279. Perfect Squares

    Given an integer n, return the least number of perfect square numbers that sum to n.

    A perfect square is an integer that is the square of an integer; in other words,
    it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
'''
import math

'''
    Accepted but time limit exceeded
    
    Note: the sequence of perfect squares that make up the sum need not be in increasing order
'''


class Solution:
    def num_squares_helper(self, n, possible_squares):
        # if the goal n is itself a perfect square then we return 1 because there's possible shortest sequence
        if n in possible_squares:
            return 1

        min_length = float('inf')

        # otherwise, we need to find the minimum length by branching out of the current position => we need to branch out of all possible squares
        for perfect_square in possible_squares:
            # if we reach a perfect square that is bigger than our goal, then we stop because the other ones will be bigger and we can't obtain
            # a sum sequence with them
            if perfect_square > n:
                break
            else:
                # we consider the perfect square and see where it goes: in this loop we consider ALL the possible squares (regardless of which ones we already examined)
                current_length = 1 + self.num_squares_helper(n - perfect_square, possible_squares)

                min_length = int(min(min_length, current_length))

        return min_length

    def numSquares(self, n: int) -> int:
        # all possible perfect squares will be from 1 to maximum n (sqrt(n) x sqrt(n))
        possible_squares = []

        for i in range(1, int(math.sqrt(n)) + 1):
            possible_squares.append(i * i)

        return self.num_squares_helper(n, possible_squares)


'''
    Time limit Exceeded
'''


class Solution2:
    def num_squares_helper(self, n, possible_squares, memo):
        # if the goal n is itself a perfect square then we return 1 because there's possible shortest sequence
        if n in possible_squares:
            memo[n] = 1

            return 1
        elif n in memo:
            return memo[n]
        else:
            min_length = float('inf')

            # otherwise, we need to find the minimum length by branching out of the current position => we need to branch out of all possible squares
            for perfect_square in possible_squares:
                # if we reach a perfect square that is bigger than our goal, then we stop because the other ones will be bigger and we can't obtain
                # a sum sequence with them
                if perfect_square > n:
                    break
                else:
                    # we consider the perfect square and see where it goes: in this loop we consider ALL the possible squares (regardless of which ones we already examined)
                    current_length = 1 + self.num_squares_helper(n - perfect_square, possible_squares, memo)

                    min_length = int(min(min_length, current_length))

            memo[n] = min_length

            return min_length

    def numSquares(self, n: int) -> int:
        memo = {}

        # all possible perfect squares will be from 1 to maximum n (sqrt(n) x sqrt(n))
        possible_squares = []

        for i in range(1, int(math.sqrt(n)) + 1):
            possible_squares.append(i * i)

        for i in range(1, n + 1):
            # we calculate the min length of all numbers leading up to n (that way their results would be saved in memo)
            self.num_squares_helper(i, possible_squares, memo)

        return memo[n]


'''
    Accepted: DP bottom-up
'''


class Solution3:
    def numSquares(self, n: int) -> int:
        # all possible perfect squares will be from 1 to maximum n (sqrt(n) x sqrt(n))
        possible_squares = []

        # cache[i] minimum length sequence to obtain sequence sum equal to i
        # we need to index cache[n] so the length should be > n
        cache = [float('inf')] * (n + 1)

        for i in range(1, int(math.sqrt(n)) + 1):
            possible_squares.append(i * i)

        # in the first loop below we will do cache[i-perfect_square] where i = 1 and perfect_square = 1 => cache[0]
        # since we don't want it to affect any result, we will initialize cache[0] to 0
        # especially that 0 is not a valid value for n
        # Also, whenever we have n as a perfect square itself, we will always refer to cache[0] because at some point in the loop
        # we will subtract n from itself since it's in possible_squares, so it's important to have cache[0] as a correct value 0
        # that way the min length of a sequence when n is a perfect square would be 1 + 0 = 1 which is correct
        cache[0] = 0

        for i in range(1, n + 1):
            for perfect_square in possible_squares:
                if i < perfect_square:
                    break
                else:
                    # instead of current_length = 1 + self.num_squares_helper(n - perfect_square, possible_squares, memo)
                    # since we update cache[i] with every iteration over possible_squares, we need cache[i] to always be a minimum
                    # so we update cache[i] as minimum of its previous value and its current value by removing the current perfect_square
                    cache[i] = int(min(cache[i], 1 + cache[i - perfect_square]))

        return cache[n]


print(Solution3().numSquares(7927))
