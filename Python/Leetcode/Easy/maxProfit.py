"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
import math


def maxProfit(price):
    if len(price) == 0:
        return 0
    elif price[0] == 0:
        return 0
    profit = 0
    buy_value = price.index(min(price))
    buy_value_index = price.index(buy_value)
    sell_array = price[buy_value_index + 1:]
    if len(sell_array) >= 1:
        sell_value = max(price[buy_value_index + 1:])
        profit = sell_value - buy_value
        if profit > 0:
            return profit
        else:
            return 0


    # print(buy_point_index)
    # print(sell_value)
print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([2, 4, 1]))
print(maxProfit([0]))


def maxProfit2(prices):
    if len(prices) == 0:
        return 0
    min_price_seen = prices[0]
    max_profit = 0

    for price in prices:
        min_price_seen = min(price, min_price_seen)
        current_profit = price - min_price_seen
        max_profit = max(current_profit, max_profit)
    return max_profit


print(maxProfit2([7, 1, 5, 3, 6, 4]))
print(maxProfit2([7, 6, 4, 3, 1]))
print(maxProfit2([2, 4, 1]))
print(maxProfit2([0]))
print(maxProfit2([]))
