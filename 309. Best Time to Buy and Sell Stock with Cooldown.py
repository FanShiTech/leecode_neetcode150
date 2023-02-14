"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]


"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        prices = [1,2,3,0,2]

        if buy  i+1
        if sell i +2



        """

        dp = {} # key = (i, buying) val = maax_profit, buying is boolean

        def dfs(index, buying):
            if index >= len(prices):
                return 0
            if (index, buying) in dp:
                return dp[(index, buying)]

            if buying:

                buy = dfs(index + 1, not buying) - prices[index]
                cooldown = dfs( index + 1, buying)
                dp[(index, buying)] = max(buy, cooldown)
            else:
                sell = dfs(index + 2, not buying) + prices[index]
                cooldown = dfs( index + 1, buying)
                dp[(index, buying)] = max(sell, cooldown)

            return dp[(index, buying)]

        return dfs(0, True)
