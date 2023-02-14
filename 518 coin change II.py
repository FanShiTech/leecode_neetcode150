"""

ou are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.



Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # o(m*n) o(m*n)
        # bottom up
        # add coins one by one m starting from base case 0 coins
        # for each added coin, compute recursively the number of combinations for each amount of money from 0 - amount
        # ex: for amount of 10, how many combination we can use based on [2,5,10],
        # [2] : 2 + 2 + 2 + 2 + 2,  [2,5] : 2 + 2 + 2 + 2 + 2 & 5, 5, [ 2,5,10]: 2 + 2 + 2 + 2 + 2 & 5, 5 & 10

        dp = [0] * (amount + 1)
        dp[0] = 1  # [1,0,0,0,0,0]
        for coin in coins:
            for x in range(coin,
                           amount + 1):  # because we start from based case 0 coins, to get to the amount 10, we can use 0 coins and its comibattion is 1
                dp[x] += dp[x - coin]  # for each amount x, the number of combinations : dp[x] += dp[x-coin]
        return dp[amount]