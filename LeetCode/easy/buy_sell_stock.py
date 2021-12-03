class Solution:
    def maxProfit(self, prices) -> int:
        # by default the buy_index is the first day and we have no profit
        buy_index = 0
        profit = 0

        for i in range(1, len(prices)):
            # now we need loop over the remaining days
            # if prices[i] >= prices[buy_index]:
            #   we are not in a day where the stock's price has risen so we can make a profit
            #   we need to check first if the profit we make from selling at day i is more than
            #   the profit we already have
            #   if (prices[i] - prices[buy_index]) > profit:
            #       sell_index = prices[i]
            #       profit = prices[sell_index] - prices[buy_index]
            #   # otherwise we don't need to do anything because what we have is better
            # else:
            #   the current price is lower than the buy price we've already seen
            #   we can potentially achieve more profit with this new price
            #   buy_index = i
            if prices[i] >= prices[buy_index]:
                if (prices[i] - prices[buy_index]) > profit:
                    profit = prices[i] - prices[buy_index]
            else:
                buy_index = i

        return profit

solution = Solution()
solution.maxProfit([7,1,5,3,6,4])