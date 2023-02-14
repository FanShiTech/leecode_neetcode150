"""

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 1

        for i in range(n - 1):
            temp = p1
            p1 = p2 + p1
            p2 = temp

        return p1
        """
        Let dp[i]dp[i]dp[i] denotes the number of ways to reach on ithi^{th}ith step:

        dp[i]=dp[i−1]+dp[i−2]

        every time we move the pointers, p1 means 2 steps at aa time, and p2 is 1 step at a time

        """