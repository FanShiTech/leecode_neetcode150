"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

def maxProfit(prices):
    min_p = float('inf')
    max_p = 0

    for i in prices:
        if prices[i] < min_p:
            min_p = prices[i]
        elif prices[i] - min_p > max_p:
            max_p = prices[i] - min_p
    return mx_p
