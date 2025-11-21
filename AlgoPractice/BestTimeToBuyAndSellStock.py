# Best time to buy and sell stock

# Understand 
# We need to find the highest possible PROFIT from buying a stock on one day and selling on next day
# profit is calculated as prices[j]-prices[i] where i is buy day and j is sell day (j>i)

# Iterate over each possible day i as the buying day
# for each buying day i, we iterate over all subsequent days j where j>i as the selling day

# for each pair (buy and sell days) calculate the profit as prices[j]-prices[i]
# if profit is positive (that stock price on day j > stock price on day i) then check if this profit is the highest so far
# return highest value for max_profit that is the answer

from typing import List

class Solution:
    def BuySell(self, prices: List[int]) -> int:
        highest = 0
        for i in range(len(prices)): # takes O(n)
            for j in range(i+1, len(prices)): # takes O(n) dependent on outer loop
                profit = prices[j]-prices[i]

                if profit > 0:
                    profit = max(highest,profit)
        return profit

# TC = O(n^2)

# Optimal 
# find out the minimum price - track lowest price encounterd so fat as we iterate through the list
# calculate profit at each step by min_price - current_price
# update max_profit - only calculate profit for current day using min price
# if profit > previous max_profit then update the max profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit


# TC = O(n)
