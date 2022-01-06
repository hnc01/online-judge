'''
    https://leetcode.com/problems/coin-change/

    322. Coin Change

    You are given an integer array coins representing coins of different denominations and an integer amount
    representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be
    made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.
'''
import math


class Solution:
    def coin_change_helper(self, coins, amount, root_coin):
        # we will do bfs starting at root index
        Q = []

        # since we're starting at root_index it means that for sure we will include it in our sequence
        amount_left = amount - root_coin

        # append the current index, amount left to produce, depth
        # we start at depth 1 because if it happens that the amount we're looking for is also an available coin
        # then we need to return 1 in that case and not 0
        Q.append((amount_left, 1))

        while len(Q) != 0:
            amount_left, depth = Q.pop(0)

            if amount_left == 0:
                # it means we arrived at a solution and since it's BFS, it means the first solution
                # we encounter is the shortest one
                return depth
            elif amount_left > 0:
                # we can still produce the amount required because we can still subtract from the total
                # these are the children of the current node
                for coin in coins:
                    Q.append((amount_left - coin, depth + 1))
            # else we stop adding children to this branch and eventually the Q will become empty

        return -1

    def coinChange(self, coins: [int], amount: int) -> int:
        if amount == 0:
            return 0

        min_length = -1

        for coin in coins:
            current_coin_min_length = self.coin_change_helper(coins, amount, coin)

            if current_coin_min_length > 0:
                if min_length == -1:
                    min_length = current_coin_min_length
                else:
                    min_length = int(min(current_coin_min_length, min_length))

        return min_length


'''
    Solution DP-Bottom Up
    
    Accepted: Same approach and solution as perfect_squares.py
'''


class Solution2:
    def coinChange(self, coins: [int], amount: int) -> int:
        # sorted in ascending order
        coins = sorted(coins)

        # cache: we need to save results since we have lots of common sub-problems
        cache = {}

        # we know that if the amount is 0, then the length of the number of coins is 0
        cache[0] = 0

        # now we build our solution from bottom up. That is, instead of solving for amount from the start,
        # we solve for 1, 2, 3, 4, until we get amount

        for target_amount in range(1, amount + 1):
            if target_amount not in cache:
                cache[target_amount] = float('inf')

            if target_amount in coins:
                cache[target_amount] = 1
            else:
                # all possible choices to consider are in coins
                for coin in coins:
                    # if a coin is more than the amount we're seeking then we can't consider it
                    if coin > target_amount:
                        break
                    else:
                        # the saved result for target_amount is always the minimum between the paths we already seen to reach target
                        # amount AND the path we're currently exploring
                        if not math.isinf(cache[target_amount - coin]):
                            cache[target_amount] = int(min(cache[target_amount], 1 + cache[target_amount - coin]))

        if math.isinf(cache[amount]):
            return -1
        else:
            return cache[amount]


'''
    Solution DP-Top down where we compute with recursion but we save the results in cache (memoization)
    
    Accepted
'''


class Solution3:
    def coin_change_helper(self, coins, amount, cache):
        # we are decreasing amount with every call so we need 2 base cases
        # one where we have amount = 0 => reached a valid sequence
        if amount == 0:
            # we return 0 because we are done with the sequence and all the 1s we added so far amount to the right value
            return 0

        # one where we have amount < 0 which means the last coin we added exceeded the amount we need
        if amount < 0:
            # we will never reach a valid amount with current sequence
            return float('inf')

        # if the amount is none of our base cases, we then checked if we computed it before
        if amount in cache:
            return cache[amount]

        # none of the above cases work so we need to do the work

        # we need to store the minimum length out of all coins
        min_length = float('inf')

        # we need to try every coin to get the target amount
        for coin in coins:
            coin_min_length = self.coin_change_helper(coins, amount - coin, cache)

            if not math.isinf(coin_min_length):
                # this means that we can obtain a valid solution with current coin
                # we need to add the 1 to min_length to account for the addition of the current coint
                min_length = int(min(min_length, 1 + coin_min_length))

        # now we have the minimum number of coins we need to build amount so we save it in memory
        cache[amount] = min_length  # which could be infinity

        return min_length

    def coinChange(self, coins: [int], amount: int) -> int:
        # obvious solutions here
        if amount == 0:
            return 0

        if amount in coins:
            return 1

        # otherwise, we need to solve the problem

        # we need cache to save already computed sub-problems
        # the idea is that we will save in cache[i] the minimum number of denominations needed to get amount i
        cache = {}

        # first we start with the base case
        # we know that if we try to build a sequence where target amount is 0, then the result will be 0
        cache[0] = 0

        # we now call the helper function to save all amounts in cache
        self.coin_change_helper(coins, amount, cache)

        if not math.isinf(cache[amount]):
            return cache[amount]
        else:
            return -1


coins = [1, 2, 5]
amount = 11

coins = [2, 4]
amount = 5
# #
coins = [1, 2, 5]
amount = 100
# # #
coins = [1]
amount = 1
# #
coins = [4, 5]
amount = 23

print(Solution3().coinChange(coins, amount))
